#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = *head, *prev = 0;
	listint_t *new;

	new = malloc(sizeof(listint_t));

	if (!new)
		return (0);

	new->n = number;
	new->next = 0;

	while(curr && curr->n < number)
	{
		prev = curr;
		curr = curr->next;
	}
	if (!prev)
	{
		*head = new;
		new->next = curr;
	}
	else
	{
		prev->next = new;
		new->next = curr;
	}
	return (new);
}
