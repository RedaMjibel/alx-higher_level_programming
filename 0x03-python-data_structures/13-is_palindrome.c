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
	struct listint_s *current = *head;
	struct listint_s *fast = *head;
	struct listint_s *middle = NULL;
	struct listint_s *temp = NULL;
	struct listint_s *previous = NULL;
	struct listint_s *rev = NULL;

	if (current == NULL || current->next == NULL)
		return (1);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next-next;
		previous = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		middle = slow;
		slow = slow->next;
	}
	previous->next = NULL;
	while (slow != NULL)
	{
		temp = slow->next;
		slow->next = rev;
		slow = temp;
	}
	while (current != NULL && rev != NULL)
	{
		if (current->n != rev->n)
			return (0);
		current = current->next;
		rev = rev->next;
	}
	return (1);
}
