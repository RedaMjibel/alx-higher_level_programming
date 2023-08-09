#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if there is a cycle
 * @list: takes a singly linked list a s parameter
 *
 * Return: true or false
 */

int check_cycle(listint_t *list)
{
	struct listint_s *slow = list;
	struct listint_s *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
