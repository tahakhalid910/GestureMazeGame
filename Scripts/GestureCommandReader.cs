using UnityEngine;
using System.IO;

public class GestureCommandReader : MonoBehaviour
{
    public PlayerMovement playerMovement;

    void Update()
    {
        string path = @"C:\Users\omair\Desktop\GestureControl\gesture_command.txt";

        if (File.Exists(path))
        {
            string command = File.ReadAllText(path).Trim().ToUpper();
            playerMovement.currentCommand = command;
        }
    }
}