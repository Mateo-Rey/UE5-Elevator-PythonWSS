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
<img width="2448" height="739" alt="image" src="https://github.com/user-attachments/assets/a4eb8c66-ca77-419a-a4d9-9c6fada019fd" />
<img width="2308" height="1086" alt="image" src="https://github.com/user-attachments/assets/a3e88bfe-b401-44e7-9acc-124d2fd150a1" />
<img width="2510" height="861" alt="image" src="https://github.com/user-attachments/assets/a483e44a-3989-43a1-abf9-fb83b51d46a7" />
<img width="2417" height="1059" alt="image" src="https://github.com/user-attachments/assets/df0d9c75-823c-4ef5-b720-ef45de8de383" />
* ElevatorPlatform
<img width="2226" height="776" alt="image" src="https://github.com/user-attachments/assets/e4a6ef0a-c62a-4cd1-8961-e090b8bbbac6" />
<img width="2364" height="1149" alt="image" src="https://github.com/user-attachments/assets/a89ea7cb-6c33-4cc7-9a50-b943fa34ce1a" />
<img width="2413" height="1002" alt="image" src="https://github.com/user-attachments/assets/bac03785-655f-4851-b17a-3f795745e68e" />
<img width="1949" height="590" alt="image" src="https://github.com/user-attachments/assets/511cbdaa-56c5-469a-9985-dfcaf345eff5" />
<img width="1809" height="1019" alt="image" src="https://github.com/user-attachments/assets/77e069ab-e135-42b9-a904-f821f95d6bf5" />
<img width="1846" height="905" alt="image" src="https://github.com/user-attachments/assets/ad41ea2b-b69b-43ae-9823-d9859e7fb16e" />
<img width="1824" height="711" alt="image" src="https://github.com/user-attachments/assets/9455f735-6e64-40d9-98c8-843fc8a3ffd5" />
<img width="2327" height="904" alt="image" src="https://github.com/user-attachments/assets/6f5cf12a-c7d9-4e09-a0ee-fc52993c5c26" />
<img width="2372" height="816" alt="image" src="https://github.com/user-attachments/assets/cce67c76-2234-4114-85f6-09a9dfa57056" />
* Functions/Variables For ElevatorPlatform
 <img width="513" height="856" alt="image" src="https://github.com/user-attachments/assets/2617f3b9-051c-4beb-ba87-93d2fe7ff711" />
<img width="1681" height="714" alt="image" src="https://github.com/user-attachments/assets/d76b216c-0908-42e3-ad78-2bd59c2e2d19" />
<img width="769" height="658" alt="image" src="https://github.com/user-attachments/assets/75b9a371-409e-44fc-9205-11b719e0d19e" />
<img width="1441" height="584" alt="image" src="https://github.com/user-attachments/assets/b4e64c9c-9200-4fc5-b2f7-ec27f885e2c5" />
<img width="2360" height="605" alt="image" src="https://github.com/user-attachments/assets/cb8d1f2b-e7d0-48a2-ae02-a55fa44b9de6" />
<img width="1735" height="536" alt="image" src="https://github.com/user-attachments/assets/a9b763b5-9e66-424a-8292-880e53fd7e1e" />
<img width="724" height="661" alt="image" src="https://github.com/user-attachments/assets/b982e171-8afa-4e8e-a365-2c6f2bf06a2d" />
<img width="2454" height="784" alt="image" src="https://github.com/user-attachments/assets/abe1ca54-5b84-4c6d-95f5-a63156313c0b" />
* Top Unload Platform
<img width="1409" height="571" alt="image" src="https://github.com/user-attachments/assets/8f4227c2-375c-45d7-b1f9-72e12b763646" />
* Gate
<img width="1216" height="483" alt="image" src="https://github.com/user-attachments/assets/4d175d27-c9ef-46f9-9c26-91a5579915cc" />
  * Click on the Timeline to edit it and add a Float Track. Add one keyframe at 0,0 and one at 1,1. After that right-click on both keyframes and set the interpolation to auto.
### 9. Key Instructions
* First run the python server, then the ui, then the game simulation. This is because the ui has to receive the dimensions event and this is only sent once the simulation begins. After that you have to start with the direction as up and are free to test with as many pawns and elevator runtime as you like!
  














