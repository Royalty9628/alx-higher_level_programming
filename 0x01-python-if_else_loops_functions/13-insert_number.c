#include "lists.h"

/**
 * insert_node - inserts a new node at a given position.
 * @head: head of a list.
 * @number: index of the list where the new node is added.
 * Return: the address of the new node, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *h;
	listint_t *prev;

	h = *head;
	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	while (h != NULL)
	{
		if (h->n > number)
			break;
		prev = h;
		h = h->next;
	}

	new->n = number;
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	else
	{
		new->next = h;
		if (h == *head)
			*head = new;
		else
			prev->next = new;
	}
	return (new);
}
