import asyncio
import threading
import websockets
import json
from tkinter import *
import uuid
import datetime
import math

# Globals
groupIdArr = None
fullFloors = {}
loop = None
websocket = None
start_time = None
data = None
event = None
stop_timer = False
timer_job = None

# Tkinter variables (initialized later)
people_var = None
time_var = None
direction_var = None
state_var = None
groupId_var = None
root = None


def generate_grid_vectors(root, rows, columns, actor_length, actor_width):
    vectors = {}
    start_x = float(root.split()[0][2:])
    start_y = float(root.split()[1][2:])
    z = float(root.split()[2][2:])

    for col in range(columns):
        for row in range(rows):
            x = start_x + (col * actor_length)
            y = (
                start_y - (row * actor_width)
                if event == "dimensions"
                else start_y + (row * actor_width)
            )
            vector_str = f"X={x:.2f} Y={y:.2f} Z={z:.2f}"
            vectors[vector_str] = vector_str

    return vectors


async def listen_for_messages(ws):
    try:
        async for json_message in ws:
            global event, data
            message = json.loads(json_message)
            receivedData = message.get("Data", {})
            state_value = receivedData.get("state")
            floor_value = receivedData.get("floor")
            groupId_value = receivedData.get("groupId")
            time_value = receivedData.get("time")
            eventType = message.get("EventType")
            event = eventType

            if eventType == "stateUpdate":

                def update_ui():
                    state_var.set(state_value)
                    time_var.set(time_value)
                    if state_value == "moving":
                        renderUI()
                        start_timer()
                    else:
                        renderUI()

                root.after(0, update_ui)
            if eventType == "floorUpdate":
                fullFloors[groupId_value] = str(int(floor_value) + 1)
            if eventType in ("dimensions", "unloadDimensions"):
                length = float(receivedData.get("platform_length"))
                width = float(receivedData.get("platform_width"))
                root_position = receivedData.get("root")
                actorLength = 200
                actorWidth = 200

                rowCount = math.floor(width / actorWidth)
                columnCount = math.floor(length / actorLength)
                grid_vectors = generate_grid_vectors(
                    root_position, rowCount, columnCount, actorLength, actorWidth
                )
                data = grid_vectors
                event = (
                    "calculateSize"
                    if eventType == "dimensions"
                    else "calculateUnloadSize"
                )
                asyncio.run_coroutine_threadsafe(send_message(), loop)

            print(f"[CLIENT RECEIVED] {message}")
    except websockets.exceptions.ConnectionClosed:
        print("[CLIENT] Connection closed")


async def start_connection():
    global websocket
    uri = "ws://localhost:8080"
    websocket = await websockets.connect(uri)
    print("[CLIENT] Connected to WebSocket")
    asyncio.create_task(listen_for_messages(websocket))


def start_async_loop():
    global loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_connection())
    loop.run_forever()


async def send_message():
    if websocket:
        message = {
            "eventType": event,
            "eventTimestamp": str(datetime.datetime.now()),
            "source": {"ClientType": "python"},
            "data": data,
        }
        await websocket.send(json.dumps(message))
        if (
            message["eventType"] == "calculateSize"
            or message["eventType"] == "calculateUnloadSize"
        ):
            print("[CLIENT SENT] Calculated Dimensions")
        else:
            print(f"[CLIENT SENT] {message}")


def reset():
    global data, stop_timer, timer_job, event, groupIdArr, fullFloors
    event = "reset"
    groupIdArr = []
    fullFloors = []
    stop_timer = True
    if timer_job is not None:
        root.after_cancel(timer_job)
        timer_job = None

    data = {"state": "reset"}
    asyncio.run_coroutine_threadsafe(send_message(), loop)

    state_var.set("newIdle")
    direction_var.set("1")
    groupId_var.set(str(uuid.uuid4()))
    renderUI()
    stop_timer = False


def start_timer():
    global timer_job
    if timer_job is not None:
        root.after_cancel(timer_job)

    def updateTime():
        global timer_job
        try:
            current_time = int(time_var.get())
        except ValueError:
            current_time = 0

        print(f"[DEBUG] Timer tick: {current_time}")

        if current_time > 0 and not stop_timer:
            current_time -= 1
            time_var.set(str(current_time))
            timer_job = root.after(1000, updateTime)
        else:
            time_var.set("0")
            timer_job = None
            print("[DEBUG] Timer complete or stopped")

    updateTime()


def sendElevator():
    global start_time, data, event, groupIdArr
    currentID = groupId_var.get()
    floor = direction_var.get()

    if floor in fullFloors.items():
        state_var.set("newIdle")
        renderUI()
        return

    if currentID not in groupIdArr:
        groupIdArr.append(currentID)

    start_time = int(time_var.get())
    event = "startElevator"
    data = {
        "state": "boarding",
        "people": people_var.get(),
        "time": time_var.get(),
        "direction": str(int(floor) - 1),
        "groupId": currentID,
    }
    asyncio.run_coroutine_threadsafe(send_message(), loop)
    groupId_var.set(str(uuid.uuid4()))
    renderUI()


def validate_input(value_if_allowed):
    if value_if_allowed == "":
        return True
    if value_if_allowed.isdigit():
        num = int(value_if_allowed)
        return 1 <= num <= 4
    return False


def switchIdle():
    if state_var.get() == "newIdle":
        state_var.set("madeIdle")
    else:
        state_var.set("newIdle")
    renderUI()


def setGroupId(groupId):
    groupId_var.set(groupId)


def renderUI():
    for widget in root.winfo_children():
        widget.destroy()

    state = state_var.get()
    vcmd = (root.register(validate_input), "%P")
    Button(root, text="Reset", command=reset).pack()
    Label(root, text="Full Floors").pack()
    for floor in fullFloors.items():
        Label(root, text=f"{floor}").pack()
    if state == "newIdle":
        Button(root, text="Move Created Group", command=switchIdle).pack()
        Label(root, text="Number of People").pack()
        Entry(root, textvariable=people_var).pack()
        Label(root, text="Enter Floor Number 1-4").pack()
        Entry(
            root, textvariable=direction_var, validate="key", validatecommand=vcmd
        ).pack()
        Label(root, text="Time of Travel").pack()
        Entry(root, textvariable=time_var).pack()
        Button(root, text="Send", command=sendElevator).pack()
    elif state == "madeIdle":
        Button(root, text="Move New Group", command=switchIdle).pack()
        Label(root, text="Click on the GroupId you wish to move").pack()
        for groupId in groupIdArr:
            Button(
                root, text=groupId, command=lambda val=groupId: setGroupId(val)
            ).pack()

        Label(root, text="Enter Floor Number 1-5").pack()
        Entry(
            root, textvariable=direction_var, validate="key", validatecommand=vcmd
        ).pack()
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

    elif state == "unloading":
        Label(root, text="Please wait while elevator unloads").pack()


def createUI():
    global people_var, time_var, direction_var, state_var, groupId_var, root, groupIdArr, fullFloors
    root = Tk()
    root.title("UI for UE5 Project")
    root.geometry("400x400")
    groupIdArr = []
    fullFloors = {}
    people_var = StringVar(value="5")
    time_var = StringVar(value="10")
    direction_var = StringVar(value="2")
    state_var = StringVar(value="newIdle")
    groupId_var = StringVar(value=str(uuid.uuid4()))

    renderUI()
    root.mainloop()


if __name__ == "__main__":
    threading.Thread(target=start_async_loop, daemon=True).start()
    createUI()
