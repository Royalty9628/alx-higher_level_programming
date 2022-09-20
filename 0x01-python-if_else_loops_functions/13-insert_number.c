#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts node in a sorted list.
 * @head: pointer to the list to be add.
 * @number: number to add.
 * Return: the list with the new number.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *tmp = *head;

	if (head == NULL)
		return (NULL);
	
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	while (tmp->next != NULL)
	{
		if (new->n >= tmp->n && new->n <= tmp->next->n)
		{
			new->next = tmp->next;
			tmp->next = new;
			return (new);
		}
		tmp = tmp->next;
	}
	return (new);
}
