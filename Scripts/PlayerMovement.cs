using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    public float moveSpeed = 5f;
    public float rotateSpeed = 120f;

    public string currentCommand = "STOP";

    void Update()
    {
        float move = 0f;

        // Forward movement
        if (Input.GetKey(KeyCode.W) || currentCommand == "FORWARD")
        {
            move = 1f;
        }

        // Backward movement
        if (Input.GetKey(KeyCode.S))
        {
            move = -1f;
        }

        // Move player
        transform.Translate(Vector3.forward * move * moveSpeed * Time.deltaTime);

        // Turn left
        if (Input.GetKey(KeyCode.A) || currentCommand == "LEFT")
        {
            transform.Rotate(Vector3.up * -rotateSpeed * Time.deltaTime);
        }

        // Turn right
        if (Input.GetKey(KeyCode.D) || currentCommand == "RIGHT")
        {
            transform.Rotate(Vector3.up * rotateSpeed * Time.deltaTime);
        }
    }
}