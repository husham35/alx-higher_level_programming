#include "lists.h"

/**
 * check_cycle - checks if a singly-linked list is a cycle.
 * @list:list to checked.
 *
 * Return: 0 if no cycle else 1 if cycle exists.
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	/* checks to see if list is null or contains only 1 node */
	if (!list || !list->next)
		return (0);

	while (slow->next && fast->next && fast->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
