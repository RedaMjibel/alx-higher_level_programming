#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the list
 *
 * Return: 1 if true or 0 if false
 */
int is_palindrome(listint_t **head)
{
	struct listint_s *slow = *head;
	struct listint_s *fast = *head;
	struct listint_s *rev = NULL;
	struct listint_s *temp = NULL;

	if ((*head) == NULL || (*head)->next == NULL)
		return 1;
	while (1)
	{
		fast = fast->next->next;
		if (fast->next == NULL)
		{
			slow = slow->next->next;
			break;
		}
		if (fast == NULL)
		{
			slow = slow->next;
			break;
		}
		slow = slow->next;
	}
	slow->next = NULL;
	while (slow != NULL)
	{
		temp = slow->next;
		slow->next = rev;
		rev = slow;
		slow = temp;
	}
	while (head != NULL && rev != NULL)
	{
		if ((*head)->n != rev->n)
			return (0);
		*head = (*head)->next;
		rev = rev->next;
	}
	return (1);
}
