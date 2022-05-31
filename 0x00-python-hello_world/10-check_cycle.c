#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - checks a list for a loop
 *
 * @list: list to be checked
 * Return: 1 if there is loop or 0 if otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	if (!list || !list->next)
		return (0);

	tortoise = hare = list;
	tortoise = tortoise->next;
	hare = hare->next->next;
	while (tortoise && hare && hare->next)
	{
		if (tortoise == hare)
			return (1); /* Loop found */
		tortoise = tortoise->next;
		hare = hare->next->next;
	}
	/* No loop/cycle found */
	return (0);
}
