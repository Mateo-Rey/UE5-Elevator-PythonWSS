import asyncio
import threading
import websockets
import json
from tkinter import *
import uuid
import datetime
import math
# Globals
loop = None
websocket = None
start_time = None
data = None
event = None
stop_timer = False # Boolean for checking if timer is stopped
timer_job = None  # This will hold the ID returned by root.after()
# Tkinter variables (initialized later)
people_var = None
time_var = None
direction_var = None
state_var = None
groupId_var = None
root = None

# Async listener
async def listen_for_messages(ws):
    try:
        async for json_message in ws:
            global event, data
            message = json.loads(json_message)
            receivedData = message.get("Data", {})
            state_value = receivedData.get("state")
            eventType = message.get("EventType")
            if eventType == "stateUpdate":
                if state_value == "moving":
                    def update_ui():
                        state_var.set(state_value)
                        renderUI()
                    root.after(0, update_ui)
                if state_value == "top_idle":
                    def update_ui():
                        state_var.set(state_value)
                        time_var.set("10")
                        direction_var.set("down")
                        renderUI()
                    root.after(0, update_ui)
                else:
                    def update_ui():
                        state_var.set(state_value)
                        time_var.set("10")
                        direction_var.set("up")
                        renderUI()
                    root.after(0, update_ui)
            if eventType == "dimensions":
                length = float(receivedData.get("platform_length"))
                width = float(receivedData.get("platform_width"))
                actorLength = 310
                actorWidth = 180
                print(length, width)
                rowCount = width/actorWidth
                columnCount = length/actorLength
                event = "calculateSize"
                data = {
                    "rowCount": math.floor(rowCount),
                    "columnCount": math.floor(columnCount),
                }
                asyncio.run_coroutine_threadsafe(send_message(), loop)
            if eventType == "unloadDimensions":
                length = float(receivedData.get("platform_length"))
                width = float(receivedData.get("platform_width"))
                actorLength = 310
                actorWidth = 180
                print(length, width)
                rowCount = width/actorWidth
                columnCount = length/actorLength
                event = "calculateUnloadSize"
                data = {
                    "rowCount": math.floor(rowCount),
                    "columnCount": math.floor(columnCount),
                }
                asyncio.run_coroutine_threadsafe(send_message(), loop)
                
                    
            print(f"[CLIENT RECEIVED] {message}")
    except websockets.exceptions.ConnectionClosed:
        print("[CLIENT] Connection closed")

# WebSocket connection
async def start_connection():
    global websocket
    uri = "ws://localhost:8080"
    websocket = await websockets.connect(uri)
    print("[CLIENT] Connected to WebSocket")
    asyncio.create_task(listen_for_messages(websocket))

# Background async loop
def start_async_loop():
    global loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_connection())
    loop.run_forever()

# Message sender
async def send_message():
    if websocket:
        message = {
            "eventType": event,
            "eventTimestamp": str(datetime.datetime.now()),
            "source": {"ClientType": "python"},
            "data": data
        }
        await websocket.send(json.dumps(message))
        print(f"[CLIENT SENT] {message}")

# UI behavior
def reset():
    global data, stop_timer, timer_job, event
    event = "reset"
    stop_timer = True

    if timer_job is not None:
        root.after_cancel(timer_job)
        timer_job = None

    data = {
        "state": "reset"
    }
    asyncio.run_coroutine_threadsafe(send_message(), loop)

    state_var.set("bottom_idle")
    direction_var.set("up")
    renderUI()
    stop_timer = False  # Optional: Only allow next timer when elevator is sent again


def updateTime():
    global timer_job
    current_time = int(time_var.get())
    if current_time > 0 and not stop_timer:
        current_time -= 1
        time_var.set(str(current_time))
        timer_job = root.after(1000, updateTime)  # Store after job ID
    else:
        time_var.set(str(5))
        timer_job = None


def sendElevator():
    global start_time
    global data
    global event
    start_time = int(time_var.get())
    event = "startElevator"
    data = {
        "state": "boarding",
        "people": people_var.get(),
        "time": time_var.get(),
        "direction": direction_var.get(),
        "groupId": groupId_var.get()
    }
    asyncio.run_coroutine_threadsafe(send_message(), loop)
    state_var.set("boarding")
    renderUI()

# Main UI rendering
def renderUI():
    for widget in root.winfo_children():
        widget.destroy()

    state = state_var.get()
    Button(root, text="Reset", command=reset).pack()

    if state == "bottom_idle" or state =="top_idle":
        Label(root, text="Number of People").pack()
        Entry(root, textvariable=people_var).pack()
        Label(root, text="Direction").pack()
        Entry(root, textvariable=direction_var).pack()
        Label(root, text="Time of Travel").pack()
        Entry(root, textvariable=time_var).pack()
        Button(root, text="Send", command=sendElevator).pack()

    elif state == "boarding":
        Label(root, text="Please wait while guests board the elevator").pack()

    elif state == "moving":
        Label(root, text="People In Transit").pack()
        Label(root, bg="green", fg="white", textvariable=people_var).pack()
        Label(root, text="Time Until Complete").pack()
        Label(root, bg="green", fg="white", textvariable=time_var).pack()
        updateTime()

    elif state == "unloading":
        Label(root, text="Please wait while elevator unloads").pack()

# Create the window and variables
def createUI():
    global people_var, time_var, direction_var, state_var, groupId_var, root
    root = Tk()
    root.title("UI for UE5 Project")
    root.geometry("400x200")

    # Initialize StringVars *after* root
    people_var = StringVar(value="5")
    time_var = StringVar(value="10")
    direction_var = StringVar(value="up")
    state_var = StringVar(value="bottom_idle")
    groupId_var = StringVar(value=str(uuid.uuid4()))

    renderUI()
    root.mainloop()

# Main
if __name__ == "__main__":
    threading.Thread(target=start_async_loop, daemon=True).start()
    createUI()
