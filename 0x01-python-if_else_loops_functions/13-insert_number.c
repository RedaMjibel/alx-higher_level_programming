#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - inserts a node into a sorted singly linked list
 * @head: the head of the singly linked list
 * @number: the number to be inserted
 *
 * Return: the adress of the new node or NULL on faliure
 */

listint_t *insert_node(listint_t **head, int number)
{
	struct listint_s *current;
	listint_t *newnode = (struct listint_s *)malloc(sizeof(struct listint_s));

	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	newnode->next = NULL;
	if (*head == NULL || number < (*head)->n)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}
	current = *head;
	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}
	newnode->next = current->next;
	current->next = newnode;
	return (newnode);
}
