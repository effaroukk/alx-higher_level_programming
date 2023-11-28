#include "lists.h"

/**
 * check_cycle - a function in C that checks if a singly linked list
 * has a cycle in it.
 * @list: the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *red, *black;

		if (!list || !list->next)
			return (0);
	red = list;
	black = list;

	while (black != NULL && red != NULL && red->next != NULL)
	{
		black = black->next;
		red = red->next->next;

		if (red == black)
		{
			return (1);
		}
	}
	return (0);

}
