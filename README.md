# unreal-python-websocketserver

This project demonstrates WebSocket communication between Python and Unreal Engine 5 using a custom plugin and Blueprint setup.

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
  ![image](https://github.com/user-attachments/assets/ff1f339e-87cd-4d51-808f-43999be6d3f7)
  ![image](https://github.com/user-attachments/assets/726b220a-cdcc-4a0c-aef1-b775164a4d2c)
  ![image](https://github.com/user-attachments/assets/ab6485a0-b255-45b6-ae56-66eb6d110e47)
  ![image](https://github.com/user-attachments/assets/14cc25ad-0d31-4f19-8821-399ce12136e7)
  ![image](https://github.com/user-attachments/assets/0108b65d-c307-4d5f-b2d7-07d6b93a240b)
* Functions/Variables
  ![image](https://github.com/user-attachments/assets/f84d3938-41d4-47d0-85b3-9b04b566016f)
  ![image](https://github.com/user-attachments/assets/f68e8ca2-c2fa-4137-a71c-8afd1d7752be)
  ![image](https://github.com/user-attachments/assets/e3ade783-e262-427b-a541-fb93f177ea8f)
  ![image](https://github.com/user-attachments/assets/b0c6d54d-0c89-45fc-84b0-38ac16e9472e)
  ![image](https://github.com/user-attachments/assets/21cc22d3-1ea2-42ee-adba-3cf3da1c1517)
  ![image](https://github.com/user-attachments/assets/07f94ac0-f665-4b63-8e71-75c8bf5eb076)
  ![image](https://github.com/user-attachments/assets/e5c1df81-ec46-4ab5-b36c-ef33a21ebbec)
  ![image](https://github.com/user-attachments/assets/59f3bab2-6a2a-41d9-b377-9c32fe7bf4ff)
* Top Unload Platform
  ![image](https://github.com/user-attachments/assets/7136f397-94ce-4ed4-9e68-d28890e1f163)
* Gate
  ![image](https://github.com/user-attachments/assets/b74c094b-4c79-42b7-a510-ec5b3f6de3b5)
  * Click on the Timeline to edit it and add a Float Track. Add one keyframe at 0,0 and one at 1,1. After that right-click on both keyframes and set the interpolation to auto.
### 9. Key Instructions
* First run the python server, then the ui, then the game simulation. This is because the ui has to receive the dimensions event and this is only sent once the simulation begins. After that you have to start with the direction as up and are free to test with as many pawns and elevator runtime as you like!
  














