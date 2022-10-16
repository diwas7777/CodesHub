// JavaScript implementation to convert the given
	// BST to Min Heap
	// structure of a node of BST
	class Node {
		constructor() {
		this.data = 0;
		this.left = null;
		this.right = null;
		}
	}

	/* Helper function that allocates a new node
	with the given data and null left and right
	pointers. */
	function getNode(data) {
		var newNode = new Node();
		newNode.data = data;
		newNode.left = newNode.right = null;
		return newNode;
	}

	// function prototype for preorder traversal
	// of the given tree

	// function for the inorder traversal of the tree
	// so as to store the node values in 'arr' in
	// sorted order
	function inorderTraversal(root) {
		if (root == null) return;

		// first recur on left subtree
		inorderTraversal(root.left);

		// then copy the data of the node
		arr.push(root.data);

		// now recur for right subtree
		inorderTraversal(root.right);
	}

	// function to convert the given BST to MIN HEAP
	// performs preorder traversal of the tree
	function BSTToMinHeap(root) {
		if (root == null) return;

		// first copy data at index 'i' of 'arr' to
		// the node
		root.data = arr[++i];

		// then recur on left subtree
		BSTToMinHeap(root.left);

		// now recur on right subtree
		BSTToMinHeap(root.right);
	}
	var arr = [];
	var i;

	// utility function to convert the given BST to
	// MIN HEAP
	function convertToMinHeapUtil(root) {
		// vector to store the data of all the
		// nodes of the BST
		i = -1;

		// inorder traversal to populate 'arr'
		inorderTraversal(root);

		// BST to MIN HEAP conversion
		BSTToMinHeap(root);
	}

	// function for the preorder traversal of the tree
	function preorderTraversal(root) {
		if (root == null) {
		return;
		}

		// first print the root's data
		document.write(root.data + " ");

		// then recur on left subtree
		preorderTraversal(root.left);

		// now recur on right subtree
		preorderTraversal(root.right);
	}

	// Driver program to test above
	// BST formation
	var root = getNode(4);
	root.left = getNode(2);
	root.right = getNode(6);
	root.left.left = getNode(1);
	root.left.right = getNode(3);
	root.right.left = getNode(5);
	root.right.right = getNode(7);

	convertToMinHeapUtil(root);
	document.write("Preorder Traversal: ");
	preorderTraversal(root);
