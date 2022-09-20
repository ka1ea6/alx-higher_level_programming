#include "lists.h"

/**
 * insert_node - inserts a node into a sorted singly linked list
 * @head: head of the singly linked list
 * @number: the number to be inserted
 * Return: address of the new node if successful, NULL if not.
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *current;
    listint_t *nextNode;
    listint_t *newNode;

    current = *head;
    if (current->n > number)
    {
        *head->n = number;
        *head->next = current;
        return &head;
    }

    newNode->n = number;
    newNode->next = NULL;
    nextNode = current->next;

    while(nextNode->next)
    {
        if (nextNode->n > number)
        {
            newNode->next = current->next;
            current->next = newNode;
            return &newNode;
        }
        nextNode = current->next->next;
        current = current->next;
    }
    nextNode->next = newNode;
    return &newNode;
}