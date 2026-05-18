import cv2
import numpy as np
import os

COMMAND_FILE = r"C:\Users\omair\Desktop\GestureControl\gesture_command.txt"

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Camera not working")
        break

    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([90, 100, 100])
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    command = "STOP"

    if contours:
        largest = max(contours, key=cv2.contourArea)

        if cv2.contourArea(largest) > 1000:
            x, y, w, h = cv2.boundingRect(largest)
            center_x = x + w // 2

            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)

            if center_x < frame.shape[1] // 3:
                command = "LEFT"
            elif center_x > frame.shape[1] * 2 // 3:
                command = "RIGHT"
            else:
                command = "FORWARD"

    try:
        with open(COMMAND_FILE, "w") as f:
            f.write(command)
    except PermissionError:
        pass

    cv2.putText(frame, command, (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)

    cv2.imshow("Gesture Control", frame)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()