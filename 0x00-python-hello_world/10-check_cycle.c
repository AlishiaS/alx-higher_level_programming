#include <stdio.h>
#include "lists.h"

/**
* check_cycle - Checks if there is cycle in a singly linked list
* @list: Address to the head node of the linked list
* Return: 0 if there is no cycle 1 if there's cycle
*/

int check_cycle(listint_t *list)
{
listint_t *x = NULL;
listint_t *y = NULL;
if (list == NULL || list->next == NULL)
return (0);

x = list->next->next;
y = list;
while (x != NULL)
{
if (x == y)
{
return (1);
}
y = y->next;
if (x->next != NULL)
x = x->next->next;
else
x = hare->next;
}
return (0);
}
