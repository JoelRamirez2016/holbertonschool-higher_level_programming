#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *curr = *head;
	int index = 0, len = 1;
	int *numbers;

	if (!*head || !(*head)->next)
		return (1);

	while ((curr = curr->next))
		len++;

	numbers = malloc(sizeof(int) * len);
	curr = *head;

	while (index < len / 2)
	{
		numbers[index] = curr->n;
		curr = curr->next;
		index++;
	}
	while (index-- > 0)
	{
		if (numbers[index] != curr->n)
		{
			free(numbers);
			return (0);
		}
		curr = curr->next;
	}

	free(numbers);
	return (1);
}
