# unreal-python-websocketserver

This project demonstrates WebSocket communication between Python and Unreal Engine 5 using a custom plugin and Blueprint setup.

## Demo
https://github.com/user-attachments/assets/4d99d49d-10ed-41b7-aa22-65f3c9a774e5

## 📦 Requirements

- Python 3.7+
- Unreal Engine 5
- WebSocketManagerPlugin for UE5

## 🛠️ Setup Instructions

### 1. Install Dependencies

Install required Python packages:

```bash
pip install asyncio websockets
```

### 2. Run Server and UI

Open two separate terminals

**Terminal 1 (WebSocket Server):**
```bash
python server.py
```

**Terminal 2 (Tkinter GUI):**
```bash
python unreal_websocket_ui.py
```

### 3. Create A New UE5 Project

- Open Unreal Engine 5
- Create a new project:
  - Type: Games
  - Template: Blank
  - Starter Content: Enabled
  - Project Type: Blueprint

### 4. Add WebSocketManagerPlugin

- Create a Plugins folder in your project directory:  
  `C:\Users\user\Documents\Unreal Projects\websocket_python\Plugins`
- Place the WebSocketManagerPlugin folder inside the Plugins directory.
- Open UE5 Project and click Edit → Plugins → Enable **WebSocketManagerPlugin**

### 5. Create Blueprints Folder

- In the Content folder of your UE5 project, create a new folder named: **Blueprints**

### 6. Create Actor Blueprint Classes

- Create 7 Actor Blueprints:
  - BottomUnloadPlatform
  - BottomUnloadRoot
  - ElevatorSlotRoot
  - TopUnloadRoot
  - Gate
  - ElevatorPlatform
  - TopUnloadPlatform

- Create one Character Blueprint:
  - Human/Character

- Use the modeling tool to make stairs that match the size of the elevator platform

### 7. Placement of Blueprints

- BottomUnloadPlatform should be placed under the floor to indicate the unload zone
- ElevatorPlatform must connect with TopPlatform when it moves up
- Add a **NavInvoker** component to the TopPlatform, ElevatorPlatform, and AI Pawns
- Add a **NavMeshBoundsVolume** to generate navigation data around platforms
- In UE5, go to **Edit → Project Settings → Runtime Generation** and set it to **Dynamic**
- Position each Root at the top-left corner of its platform for correct grid generation

### 8. Follow Blueprint Setup Below

#### 🧍 Human/Character Blueprint

<details>
<summary>Click to expand</summary>

<img width="2448" height="739" alt="Human 1" src="https://github.com/user-attachments/assets/a4eb8c66-ca77-419a-a4d9-9c6fada019fd" />
<img width="2308" height="1086" alt="Human 2" src="https://github.com/user-attachments/assets/a3e88bfe-b401-44e7-9acc-124d2fd150a1" />
<img width="2510" height="861" alt="Human 3" src="https://github.com/user-attachments/assets/a483e44a-3989-43a1-abf9-fb83b51d46a7" />
<img width="2417" height="1059" alt="Human 4" src="https://github.com/user-attachments/assets/df0d9c75-823c-4ef5-b720-ef45de8de383" />

</details>

#### 🛗 ElevatorPlatform Blueprint

<details>
<summary>Click to expand</summary>

<img width="2226" height="776" alt="Elevator 1" src="https://github.com/user-attachments/assets/e4a6ef0a-c62a-4cd1-8961-e090b8bbbac6" />
<img width="2364" height="1149" alt="Elevator 2" src="https://github.com/user-attachments/assets/a89ea7cb-6c33-4cc7-9a50-b943fa34ce1a" />
<img width="2413" height="1002" alt="Elevator 3" src="https://github.com/user-attachments/assets/bac03785-655f-4851-b17a-3f795745e68e" />
<img width="1949" height="590" alt="Elevator 4" src="https://github.com/user-attachments/assets/511cbdaa-56c5-469a-9985-dfcaf345eff5" />
<img width="1809" height="1019" alt="Elevator 5" src="https://github.com/user-attachments/assets/77e069ab-e135-42b9-a904-f821f95d6bf5" />
<img width="1846" height="905" alt="Elevator 6" src="https://github.com/user-attachments/assets/ad41ea2b-b69b-43ae-9823-d9859e7fb16e" />
<img width="1824" height="711" alt="Elevator 7" src="https://github.com/user-attachments/assets/9455f735-6e64-40d9-98c8-843fc8a3ffd5" />
<img width="2327" height="904" alt="Elevator 8" src="https://github.com/user-attachments/assets/6f5cf12a-c7d9-4e09-a0ee-fc52993c5c26" />
<img width="2372" height="816" alt="Elevator 9" src="https://github.com/user-attachments/assets/cce67c76-2234-4114-85f6-09a9dfa57056" />

</details>

#### 🔧 ElevatorPlatform: Functions & Variables

<details>
<summary>Click to expand</summary>

<img width="513" height="856" alt="Var 1" src="https://github.com/user-attachments/assets/2617f3b9-051c-4beb-ba87-93d2fe7ff711" />
<img width="1681" height="714" alt="Var 2" src="https://github.com/user-attachments/assets/d76b216c-0908-42e3-ad78-2bd59c2e2d19" />
<img width="769" height="658" alt="Var 3" src="https://github.com/user-attachments/assets/75b9a371-409e-44fc-9205-11b719e0d19e" />
<img width="1441" height="584" alt="Var 4" src="https://github.com/user-attachments/assets/b4e64c9c-9200-4fc5-b2f7-ec27f885e2c5" />
<img width="2360" height="605" alt="Var 5" src="https://github.com/user-attachments/assets/cb8d1f2b-e7d0-48a2-ae02-a55fa44b9de6" />
<img width="1735" height="536" alt="Var 6" src="https://github.com/user-attachments/assets/a9b763b5-9e66-424a-8292-880e53fd7e1e" />
<img width="724" height="661" alt="Var 7" src="https://github.com/user-attachments/assets/b982e171-8afa-4e8e-a365-2c6f2bf06a2d" />
<img width="2454" height="784" alt="Var 8" src="https://github.com/user-attachments/assets/abe1ca54-5b84-4c6d-95f5-a63156313c0b" />

</details>

#### 🟪 TopUnloadPlatform

<details>
<summary>Click to expand</summary>

<img width="1409" height="571" alt="TopUnload" src="https://github.com/user-attachments/assets/8f4227c2-375c-45d7-b1f9-72e12b763646" />

</details>

#### 🚪 Gate

<details>
<summary>Click to expand</summary>

<img width="1216" height="483" alt="Gate" src="https://github.com/user-attachments/assets/4d175d27-c9ef-46f9-9c26-91a5579915cc" />

> 💡 **Timeline Setup:** Click on the Timeline to edit it and add a Float Track. Add one keyframe at `0,0` and one at `1,1`. Then right-click on both and set interpolation to **Auto**.

</details>

### 9. Key Instructions

- **Start Order:**
  * Run the Python WebSocket server
  * Run the UI (`unreal_websocket_ui.py`)
  * Start the UE5 simulation

- The UI listens for a one-time `dimensions` event that only fires when the simulation begins.

- Start the elevator with **upward** direction.

- Feel free to test with multiple pawns and various elevator runtimes.
