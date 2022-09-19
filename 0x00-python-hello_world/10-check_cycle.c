#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if singly linked list is a cycle
 * Return: 0 if no cycle, 1 is yes
*/

int check_cycle(listint_t *list)
{
	listint_t *fast = list;
