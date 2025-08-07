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

Terminal 1 (WebSocket Server):
```bash
python server.py
```

Terminal 2 (Tkinter GUI):
```bash
python unreal_websocket_ui.py
```

### 3. Create A New UE5 Project
* Open Unreal Engine 5
* Create a new project:

  * Type: Games
  * Template: Blank
  * Starter Content: Enabled
  * Project Type: Blueprint
### 4. Add WebSocketManagerPlugin
* Create a Plugins folder in your project directory
 * C:\Users\user\Documents\Unreal Projects\websocket_python\Plugins
* Place the WebSocketManagerPlugin folder inside the Plugins directory.
* Open UE5 Project and click Edit -> Plugins -> Check Off WebSocketManagerPlugin

### 5. Create Blueprints Folder
* In the Content folder of your UE5 project, create a new folder named: Blueprints

### 6. Create Actor Blueprint Classes
* Create 7 Actor Blueprints
  * BottomUnloadPlatform
  * BottomUnloadRoot
  * ElevatorSlotRoot
  * TopUnloadRoot
  * Gate
  * ElevatorPlatform
  * TopUnloadPlatform
* Create one Character Blueprint
    * Human/Character
* Using the modeling tool to make stairs that are the size of the elevator platform
### 7. Placement of Blueprints
* Most placements are subjective but the BottomUnloadPlatform should be under the floor as an indicator of the unload zone and the ElevatorPlatform must connect with the TopPlatform once it moves up.
* Additionally the TopPlatform and ElevatorPlatform must have a NavInvoker component added, along with the AI Pawns, so that when you add a NavMeshBound it will generate on and around the platforms.
* For the NavMeshBound to generate as the pawns move go to Edit->Project Settings->Search for Runtime Generation->Set to Dynamic
* Lastly the Roots must be placed on the top left corner of each platform since the rows and columns for the grid are generated left to right and top to bottom
### 8. Follow Blueprint Setup Below
* Human/Character
  <img width="2448" height="739" alt="image" src="https://github.com/user-attachments/assets/f94c2aad-36e9-4ec3-8129-7dd248482415" />

* ElevatorPlatform
  
* Functions/Variables For ElevatorPlatform
 
* Top Unload Platform
  
* Gate
  
  * Click on the Timeline to edit it and add a Float Track. Add one keyframe at 0,0 and one at 1,1. After that right-click on both keyframes and set the interpolation to auto.
### 9. Key Instructions
* First run the python server, then the ui, then the game simulation. This is because the ui has to receive the dimensions event and this is only sent once the simulation begins. After that you have to start with the direction as up and are free to test with as many pawns and elevator runtime as you like!
  














