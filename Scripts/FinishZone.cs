using UnityEngine;

public class FinishZone : MonoBehaviour
{
    private void OnTriggerEnter(Collider other)
    {
        Debug.Log("Something entered finish zone: " + other.name);

        if (other.CompareTag("Player"))
        {
            Debug.Log("YOU ESCAPED!");
        }
    }
}