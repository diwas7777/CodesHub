// C++ program to count number of nodes in a circular
// linked list.
#include <bits/stdc++.h>
using namespace std;

/*structure for a node*/

struct Node {
	int data;
	Node* next;
	Node(int x)
	{
		data = x;
		next = NULL;
	}
};
/* Function to insert a node at the beginning
of a Circular linked list */
struct Node* push(struct Node* last, int data)
{
	if (last == NULL) {
		struct Node* temp
			= (struct Node*)malloc(sizeof(struct Node));

		// Assigning the data.
		temp->data = data;
		last = temp;
		// Note : list was empty. We link single node
		// to itself.
		temp->next = last;

		return last;
	}

	// Creating a node dynamically.
	struct Node* temp
		= (struct Node*)malloc(sizeof(struct Node));

	// Assigning the data.
	temp->data = data;

	// Adjusting the links.
	temp->next = last->next;
	last->next = temp;

	return last;
}

/* Function to count nodes in a given Circular
linked list */

int countNodes(Node* head)
{
	Node* temp = head;
	int result = 0;
	if (head != NULL) {
		do {
			temp = temp->next;
			result++;
		} while (temp != head);
	}

	return result;
}

/* Driver program to test above functions */
int main()
{
	/* Initialize lists as empty */
	Node* head = NULL;
	head = push(head, 12);
	head = push(head, 56);
	head = push(head, 2);
	head = push(head, 11);
	cout << countNodes(head);
	return 0;
}
