# Gesture Maze Game

A Unity 3D maze game controlled using computer-vision gesture commands.

## Features
- 3D maze environment
- Player movement and wall collision
- Camera follow system
- Finish zone / win condition
- Python OpenCV gesture controller
- Unity reads gesture commands from gesture_command.txt
- Keyboard fallback controls

## Controls
Keyboard:
W = forward
A = left
S = back
D = right

Gesture:
Blue object left = LEFT
Blue object center = FORWARD
Blue object right = RIGHT
No object = STOP

## How to run
1. Open the Unity project.
2. Open the MazeGame scene.
3. Run the Python script:
   py -3.11 gesture_control.py
4. Press Play in Unity.
5. Move the blue object in front of the webcam.

## Technologies
Unity, C#, Python, OpenCV
