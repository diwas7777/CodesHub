// C++ implementation of the approach
#include <bits/stdc++.h>
using namespace std;

// Structure of binary tree
struct Node {
	Node* left;
	Node* right;
	int hd;
	int data;
};

// Function to create a new node
Node* newNode(int key)
{
	Node* node = new Node();
	node->left = node->right = NULL;
	node->data = key;
	return node;
}

// Function that returns the sum of
// nodes in top view of binary tree
int SumOfTopView(Node* root)
{
	if (root == NULL)
		return 0;

	queue<Node*> q;

	map<int, int> m;
	int hd = 0;

	root->hd = hd;

	int sum = 0;

	// Push node and horizontal distance to queue
	q.push(root);

	while (q.size()) {
		hd = root->hd;

		// Count function returns 1 if the container
		// contains an element whose key is equivalent
		// to hd, or returns zero otherwise.
		if (m.count(hd) == 0) {
			m[hd] = root->data;
			sum += m[hd];
		}
		if (root->left) {
			root->left->hd = hd - 1;
			q.push(root->left);
		}
		if (root->right) {
			root->right->hd = hd + 1;
			q.push(root->right);
		}
		q.pop();
		root = q.front();
	}

	return sum;
}

// Driver code
int main()
{
	Node* root = newNode(1);
	root->left = newNode(2);
	root->right = newNode(3);
	root->left->right = newNode(4);
	root->left->right->right = newNode(5);
	root->left->right->right->right = newNode(6);

	cout << SumOfTopView(root);

	return 0;
}
