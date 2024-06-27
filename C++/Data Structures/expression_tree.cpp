// C++ program for expression tree
#include <bits/stdc++.h>
using namespace std;
class node {
public:
	char value;
	node* left;
	node* right;
	node* next = NULL;
	node(char c)
	{
		this->value = c;
		left = NULL;
		right = NULL;
	}
	node()
	{
		left = NULL;
		right = NULL;
	}
	friend class Stack;
	friend class expression_tree;
};
class Stack {
	node* head = NULL;

public:
	void push(node*);
	node* pop();
	friend class expression_tree;
};
class expression_tree {
public:
	void inorder(node* x)
	{
		// cout<<"Tree in InOrder Traversal is: "<<endl;
		if (x == NULL)
			return;
		else {
			inorder(x->left);
			cout << x->value << " ";
			inorder(x->right);
		}
	}
};

void Stack::push(node* x)
{
	if (head == NULL) {
		head = x;
	}
	// We are inserting here nodes at the top of the stack [following LIFO principle]
	else {
		x->next = head;
		head = x;
	}
}
node* Stack::pop()
{
	// Popping out the top most[ pointed with head] element
	node* p = head;
	head = head->next;
	return p;
}
int main()
{
	string s = "ABC*+D/";
	// If you wish take input from user:
	//cout << "Insert Postorder Expression: " << endl;
	//cin >> s;
	Stack e;
	expression_tree a;
	node *x, *y, *z;
	int l = s.length();
	for (int i = 0; i < l; i++) {
		// if read character is operator then popping two
		// other elements from stack and making a binary
		// tree
		if (s[i] == '+' || s[i] == '-' || s[i] == '*'
			|| s[i] == '/' || s[i] == '^') {
			z = new node(s[i]);
			x = e.pop();
			y = e.pop();
			z->left = y;
			z->right = x;
			e.push(z);
		}
		else {
			z = new node(s[i]);
			e.push(z);
		}
	}
	cout << " The Inorder Traversal of Expression Tree: ";
	a.inorder(z);
	return 0;
}
