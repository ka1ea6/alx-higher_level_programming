#include "lists.h"

/**
 * is_palindrome - checks if a signly linked list is a palindrome
 *
 * @head: pointer to the head of the list.
 * Return: 0 if it is not a palindrome, 1 if it is.
 */

int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head, *dup = *head, *temp = *head;

	if (*head == NULL ||  (*head)->next == NULL)
		return (1);
	
	while (1)
	{
		fast = fast->next->next;

		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}

		slow = slow->next;
	}

	reverse_list(&dup);

	while(dup && temp)
	{
		if (dup->n != temp->n)
			return (0);
		dup = dup->next;
		temp = temp->next;
	}
	if (!dup)
		return (1);
	

	return (0);
}

/*
 * reverse_list - reverses a singly linked list
 *
 * @head: head of the linked list to be reversed.
 * Return: nothing.
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

