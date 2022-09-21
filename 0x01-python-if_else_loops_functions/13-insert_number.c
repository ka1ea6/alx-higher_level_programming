#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
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

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);

	newNode->n = number;
	newNode->next = NULL;
	if (*head == NULL)
	{
		*head = newNode;
		return (*head);
	}
	current = *head;
	if (current->n > number)
	{
		newNode->next = current;
		return (newNode);
	}
	nextNode = current->next;

	while(nextNode->next)
	{
		if (nextNode->n > number)
			{
				newNode->next = current->next;
				current->next = newNode;
				return (newNode);
			}
		nextNode = current->next->next;
		current = current->next;
	}
	nextNode->next = newNode;
	return (newNode);
}
