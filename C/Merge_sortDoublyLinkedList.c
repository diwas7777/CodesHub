#include <stdio.h>
#include <stdlib.h>
struct Node
{
    int data;
    struct Node *next, *prev;
};

struct Node *split(struct Node *head);

struct Node *merge(struct Node *first, struct Node *second)
{

    if (!first)
        return second;

    if (!second)
        return first;

    if (first->data < second->data)
    {
        first->next = merge(first->next, second);
        first->next->prev = first;
        first->prev = NULL;
        return first;
    }
    else
    {
        second->next = merge(first, second->next);
        second->next->prev = second;
        second->prev = NULL;
        return second;
    }
}

struct Node *mergeSort(struct Node *head)
{
    if (!head || !head->next)
        return head;
    struct Node *second = split(head);

    head = mergeSort(head);
    second = mergeSort(second);

    return merge(head, second);
}

void insert(struct Node **head, int data)
{
    struct Node *temp =
        (struct Node *)malloc(sizeof(struct Node));
    temp->data = data;
    temp->next = temp->prev = NULL;
    if (!(*head))
        (*head) = temp;
    else
    {
        temp->next = *head;
        (*head)->prev = temp;
        (*head) = temp;
    }
}

void print(struct Node *head)
{
    struct Node *temp = head;
    printf("\nForward Traversal using next poitner\n");
    while (head)
    {
        printf("%d ", head->data);
        temp = head;
        head = head->next;
    }
    printf("\nBackward Traversal using prev pointer\n");
    while (temp)
    {
        printf("%d ", temp->data);
        temp = temp->prev;
    }
}

void swap(int *A, int *B)
{
    int temp = *A;
    *A = *B;
    *B = temp;
}

struct Node *split(struct Node *head)
{
    struct Node *fast = head, *slow = head;
    while (fast->next && fast->next->next)
    {
        fast = fast->next->next;
        slow = slow->next;
    }
    struct Node *temp = slow->next;
    slow->next = NULL;
    return temp;
}

int main(void)
{
    struct Node *head = NULL;
    int data;
    char ch;

    do
    {
        printf("\nSelect one of the operations::");
        printf("\n1. To insert a new node in the Doubly Linked List.");
        printf("\n2. To display the nodes of the Doubly Linked List.");
        printf("\n3. To perform Merge sort on the Doubly Linked List.\n");

        int choice;
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            printf("\nEnter the value of the node to be inserted\n");
            scanf("%d", &data);
            insert(&head, data);
            break;
        case 2:
            printf("\nContents of the Doubly Linked List are::\n");
            print(head);
            break;
        case 3:
            printf("\nMerge sort applied successfully on the Doubly Linked List.\n");
            head = mergeSort(head);
            break;
        default:
            printf("Wrong Entry\n");
            break;
        }

        printf("\nDo you want to continue (Type y or n)\n");
        scanf(" %c", &ch);
    } while (ch == 'Y' || ch == 'y');
    return 0;
}