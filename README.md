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
  ![image](https://github.com/user-attachments/assets/94fbe2cb-a288-4a11-b310-732a25a35a18)
  ![image](https://github.com/user-attachments/assets/243e055b-d2aa-41b2-a052-b94893b13f17)
  ![image](https://github.com/user-attachments/assets/65ab0d83-a744-408a-8160-3a2569eb2321)
* ElevatorPlatform
  ![image](https://github.com/user-attachments/assets/5179919a-8a8d-4cec-8c30-3fb9cd936720)
  ![image](https://github.com/user-attachments/assets/034eeb8c-2fd1-421b-b769-0cc38e2b78ee)
  ![image](https://github.com/user-attachments/assets/cf4d6ec7-f7d9-4b2a-8016-0240c29c0129)
  ![image](https://github.com/user-attachments/assets/415bcbb4-a661-4521-80e9-9eb18435934c)
  ![image](https://github.com/user-attachments/assets/b34a1bc8-cb41-4a9a-9e95-7487c2da5d35)
* Functions/Variables For ElevatorPlatform
  ![image](https://github.com/user-attachments/assets/3d8ea6d4-5908-4858-88d3-339ed4bfe88a)
  ![image](https://github.com/user-attachments/assets/64850982-8e9d-4ee2-bcc6-f4ff3e6ee7f6)
  ![image](https://github.com/user-attachments/assets/0a4c27f4-1dd9-42f6-8a25-33135dba42a6)
  ![image](https://github.com/user-attachments/assets/9b7c0da4-c983-481f-87f0-0074d1ee0e99)
  ![image](https://github.com/user-attachments/assets/40258ab6-596f-4da3-9724-f8d1af915dd7)
  ![image](https://github.com/user-attachments/assets/215ce2ce-ea60-4a58-828d-98c07323a4f4)
* Top Unload Platform
  ![image](https://github.com/user-attachments/assets/7136f397-94ce-4ed4-9e68-d28890e1f163)
* Gate
  ![image](https://github.com/user-attachments/assets/b74c094b-4c79-42b7-a510-ec5b3f6de3b5)
  * Click on the Timeline to edit it and add a Float Track. Add one keyframe at 0,0 and one at 1,1. After that right-click on both keyframes and set the interpolation to auto.
### 9. Key Instructions
* First run the python server, then the ui, then the game simulation. This is because the ui has to receive the dimensions event and this is only sent once the simulation begins. After that you have to start with the direction as up and are free to test with as many pawns and elevator runtime as you like!
  














