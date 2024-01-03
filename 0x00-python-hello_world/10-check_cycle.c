#include "lists.h"

/**
 * check_cycle - checks singly linked list
 * @list: pointer
 * Return: 0 if no cycle found, else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *cur, *ch;

	if (list == NULL || list->next == NULL)
		return (0);
	cur = list;
	ch = cur->next;

	while (cur != NULL && ch->next != NULL
		&& ch->next->next != NULL)
	{
		if (cur == ch)
			return (1);
		cur = cur->next;
		ch = ch->next->next;
	}
	return (0);
}
