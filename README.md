# UE5-Elevator-PythonWSS

This project demonstrates WebSocket communication between Python and Unreal Engine 5 using a custom plugin and Blueprint setup.

## Demo
https://github.com/user-attachments/assets/f10af419-8c20-45e5-bdff-1236dac8c01b
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
  - Gate
  - ElevatorPlatform
  - TopPlatform
  - TopUnloadSlot
- Create one Character Blueprint:
  - Human/Character

- Use the modeling tool to make stairs that match the size of the elevator platform

### 7. Placement of Blueprints

- BottomUnloadPlatform should be placed under the floor to indicate the unload zone
- Add a **NavInvoker** component to the TopPlatform, ElevatorPlatform, and AI Pawns
- Add a **NavMeshBoundsVolume** to generate navigation data around platforms
- In UE5, go to **Edit → Project Settings → Runtime Generation** and set it to **Dynamic**
- Position each Root at the top-left corner of its platform for correct grid generation

### 8. Follow Blueprint Setup Below

#### 🧍 Human/Character Blueprint

<details>
<summary>Click to expand</summary>
<img width="2336" height="974" alt="image" src="https://github.com/user-attachments/assets/27ca238a-7bbb-4300-b437-8eba4e36adcc" />
<img width="2481" height="608" alt="image" src="https://github.com/user-attachments/assets/07a0f639-d543-426e-b40c-62a7b2687b7c" />
<img width="2424" height="814" alt="image" src="https://github.com/user-attachments/assets/ef01c491-dce9-469c-983b-07a059df223e" />
<img width="2509" height="785" alt="image" src="https://github.com/user-attachments/assets/7464a647-28c9-4152-98b7-754970c25b1f" />
<img width="1110" height="402" alt="image" src="https://github.com/user-attachments/assets/696735ba-29bf-4695-8275-1732cf433944" />
</details>

#### 🛗 ElevatorPlatform Blueprint

<details>
<summary>Click to expand</summary>
<img width="2335" height="747" alt="image" src="https://github.com/user-attachments/assets/feb54237-e42b-46c6-86dc-dd7649ac9608" />
<img width="2270" height="1119" alt="image" src="https://github.com/user-attachments/assets/0547459e-a3d7-47d8-8e8d-16ecd00e48c4" />
<img width="1817" height="1045" alt="image" src="https://github.com/user-attachments/assets/b1040922-0b0d-4d9e-8633-ff5ad84db889" />
<img width="2271" height="737" alt="image" src="https://github.com/user-attachments/assets/55e082c7-2717-4ca8-883d-f19ca447545f" />
<img width="2320" height="886" alt="image" src="https://github.com/user-attachments/assets/7f66a1d6-fe9e-471c-888d-adb6504316af" />
<img width="2364" height="470" alt="image" src="https://github.com/user-attachments/assets/950f6a33-7fce-40c8-89d0-381aa6ff3859" />
<img width="2519" height="553" alt="image" src="https://github.com/user-attachments/assets/31916e94-d4b6-4833-b9f0-7dffb5b4fcb8" />
<img width="2522" height="906" alt="image" src="https://github.com/user-attachments/assets/7b731ba9-7bf5-41e5-bbc6-cfe05adcac01" />
<img width="2351" height="689" alt="image" src="https://github.com/user-attachments/assets/0f4ff483-3db2-4219-83b8-ea435ad0d9a6" />
<img width="2486" height="932" alt="image" src="https://github.com/user-attachments/assets/3cdf8a53-8650-45e7-8fe2-0438cd8ca32d" />
<img width="2045" height="672" alt="image" src="https://github.com/user-attachments/assets/6b33bce5-3f16-4c24-b894-a22404dfbc74" />
</details>

#### 🔧 ElevatorPlatform: Functions & Variables

<details>
<summary>Click to expand</summary>
<img width="519" height="1221" alt="image" src="https://github.com/user-attachments/assets/a9fb60f8-812d-4283-92ce-53b03d9d8bca" />
<img width="1699" height="604" alt="image" src="https://github.com/user-attachments/assets/e85b9c40-c411-43b4-957d-6abe7943edaf" />
<img width="718" height="570" alt="image" src="https://github.com/user-attachments/assets/5a1ee092-9950-403a-aef1-2da8487f5115" />
<img width="1363" height="455" alt="image" src="https://github.com/user-attachments/assets/5b479d48-a637-42da-87fb-aa29da91927d" />
<img width="2393" height="550" alt="image" src="https://github.com/user-attachments/assets/2e8e1ee1-90d5-4303-8220-65276464da0f" />
<img width="1875" height="714" alt="image" src="https://github.com/user-attachments/assets/2d1df7c5-32c4-4fa6-aa62-0abf4aa33fb6" />
<img width="622" height="503" alt="image" src="https://github.com/user-attachments/assets/d00e7f60-1f07-4284-82fc-f3a9e8e63658" />
<img width="2488" height="854" alt="image" src="https://github.com/user-attachments/assets/02d497af-e316-4f9d-8ca7-d0ffd66b26ce" />
</details>

#### 🚪 Gate
<details>
<summary>Click to expand</summary>
<img width="1539" height="616" alt="image" src="https://github.com/user-attachments/assets/0ba387e3-7a9d-444e-96d7-6f00457ed732" />
<img width="1815" height="570" alt="image" src="https://github.com/user-attachments/assets/163ce819-f3df-450a-8196-63287e841a89" />
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
