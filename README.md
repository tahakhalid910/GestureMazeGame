# Gesture Maze Game

A lightweight 3D maze game controlled by webcam-based colour gesture recognition. A Python/OpenCV script detects a blue object in the webcam stream and writes a directional command (`LEFT`, `RIGHT`, `FORWARD`, `STOP`) to a shared text file. A Unity C# script reads this file every frame and moves the player through a 3D maze with walls, collision, a following camera, and a finish zone.

---

## System Architecture

```
Webcam → Python/OpenCV → gesture_command.txt → Unity C# → Player Movement
```

- **Python layer**: Captures frames, converts to HSV, thresholds for blue, extracts largest contour, maps horizontal position to command
- **Bridge**: `gesture_command.txt` — a plain text file containing the current command
- **Unity layer**: Reads the command file every frame and drives player movement

---

## Features

- 3D maze environment with obstacle walls and collision
- Webcam-based blue object tracking (no specialist hardware required)
- Four gesture commands: LEFT, RIGHT, FORWARD, STOP
- Keyboard fallback controls (W / A / S / D)
- Camera follow system
- Finish zone with win condition

---

## Requirements

### Python
- Python 3.11
- See `requirements.txt` for dependencies

Install dependencies:
```bash
pip install -r requirements.txt
```

### Unity
- Unity 2022.3 LTS or later
- No additional Unity packages required

### Hardware
- Any standard USB or built-in webcam
- A blue coloured object (e.g. a blue marker cap, blue tape, or any solid blue item)

---

## Known Limitation

The file path to `gesture_command.txt` is currently hardcoded in both `gesture_control.py` and `GestureCommandReader.cs`. Before running, you must update the path in both files to match your local machine. Future work will replace this with a configurable path or socket-based communication.

**In `gesture_control.py`:**
```python
COMMAND_FILE = r"C:\Your\Path\Here\gesture_command.txt"
```

**In `GestureCommandReader.cs`:**
```csharp
string path = @"C:\Your\Path\Here\gesture_command.txt";
```

Both must point to the same file.

---

## How to Run

1. Clone or download this repository
2. Update the hardcoded file path in `gesture_control.py` and `GestureCommandReader.cs` to match your system (see above)
3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Open the Unity project and load the `MazeGame` scene
5. Run the Python gesture script:
   ```bash
   py -3.11 GestureControl/gesture_control.py
   ```
6. Press **Play** in Unity
7. Hold a blue object in front of your webcam to control the player

---

## Controls

| Input | Action |
|---|---|
| Blue object — left third of frame | Turn LEFT |
| Blue object — centre of frame | Move FORWARD |
| Blue object — right third of frame | Turn RIGHT |
| No blue object detected | STOP |
| W | Move forward (keyboard fallback) |
| A | Turn left (keyboard fallback) |
| S | Move backward (keyboard fallback) |
| D | Turn right (keyboard fallback) |

---

## Project Structure

```
GestureMazeGame/
├── GestureControl/
│   ├── gesture_control.py       # Python webcam and colour tracking script
│   └── gesture_command.txt      # Shared command bridge file
├── Scripts/
│   ├── PlayerMovement.cs        # Handles player movement and rotation
│   ├── GestureCommandReader.cs  # Reads command file and updates player
│   ├── CameraFollow.cs          # Keeps camera behind and above player
│   └── FinishZone.cs            # Detects when player reaches finish
├── Scenes/
│   └── MazeGame.unity           # Main playable maze scene
├── requirements.txt
└── README.md
```

---

## Key Parameters

| Parameter | Value | Description |
|---|---|---|
| HSV lower blue | [90, 100, 100] | Lower bound for blue detection |
| HSV upper blue | [130, 255, 255] | Upper bound for blue detection |
| Min contour area | 1000 px | Filters out small noise |
| Left boundary | Frame width / 3 | LEFT command threshold |
| Right boundary | Frame width × 2/3 | RIGHT command threshold |
| Move speed | 5 units/s | Player forward speed in Unity |
| Rotate speed | 120 deg/s | Player rotation speed in Unity |

---

## Technologies

| Component | Technology |
|---|---|
| Vision processing | Python 3.11, OpenCV, NumPy |
| Game engine | Unity 2022.3, C# |
| Communication | Text file bridge |

---

## Authors

Taha Khalid Parvat Bhusal Abhinav Gyawali — Edinburgh Napier University (SET10120)