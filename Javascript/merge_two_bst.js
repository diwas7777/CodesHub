<script>

	// JavaScript program to Merge Two
	// Balanced Binary Search Trees
	// A binary tree node
	class Node {
		constructor(d) {
		this.data = d;
		this.left = null;
		this.right = null;
		}
	}

	class BinarySearchTree {
		// Constructor
		constructor() {
		this.root = null;
		}

		// Inorder traversal of the tree
		inorder() {
		this.inorderUtil(this.root);
		}

		// Utility function for inorder traversal of the tree
		inorderUtil(node) {
		if (node == null) {
			return;
		}

		this.inorderUtil(node.left);
		document.write(node.data + " ");
		this.inorderUtil(node.right);
		}

		// A Utility Method that stores
		// inorder traversal of a tree
		storeInorderUtil(node, list) {
		if (node == null) {
			return list;
		}

		//recur on the left child
		this.storeInorderUtil(node.left, list);

		// Adds data to the list
		list.push(node.data);

		//recur on the right child
		this.storeInorderUtil(node.right, list);

		return list;
		}

		// Method that stores inorder traversal of a tree
		storeInorder(node) {
		var list1 = [];
		var list2 = this.storeInorderUtil(node, list1);
		return list2;
		}

		// Method that merges two ArrayLists into one.
		merge(list1, list2, m, n) {
		// list3 will contain the merge of list1 and list2
		var list3 = [];
		var i = 0;
		var j = 0;

		//Traversing through both ArrayLists
		while (i < m && j < n) {
			// Smaller one goes into list3
			if (list1[i] < list2[j]) {
			list3.push(list1[i]);
			i++;
			} else {
			list3.push(list2[j]);
			j++;
			}
		}

		// Adds the remaining elements of list1 into list3
		while (i < m) {
			list3.push(list1[i]);
			i++;
		}

		// Adds the remaining elements of list2 into list3
		while (j < n) {
			list3.push(list2[j]);
			j++;
		}
		return list3;
		}

		// Method that converts an ArrayList to a BST
		ALtoBST(list, start, end) {
		// Base case
		if (start > end) {
			return null;
		}

		// Get the middle element and make it root
		var mid = parseInt((start + end) / 2);
		var node = new Node(list[mid]);

		/* Recursively construct the left subtree and make it
		left child of root */
		node.left = this.ALtoBST(list, start, mid - 1);

		/* Recursively construct the right subtree and make it
		right child of root */
		node.right = this.ALtoBST(list, mid + 1, end);

		return node;
		}

		// Method that merges two trees into a single one.
		mergeTrees(node1, node2) {
		//Stores Inorder of tree1 to list1
		var list1 = this.storeInorder(node1);

		//Stores Inorder of tree2 to list2
		var list2 = this.storeInorder(node2);

		// Merges both list1 and list2 into list3
		var list3 =
		this.merge(list1, list2, list1.length, list2.length);

		//Eventually converts the merged list into resultant BST
		var node = this.ALtoBST(list3, 0, list3.length - 1);
		return node;
		}
	}
	// Driver function
	/* Creating following tree as First balanced BST
				100
				/ \
				50 300
				/ \
			20 70
		*/

	var tree1 = new BinarySearchTree();
	tree1.root = new Node(100);
	tree1.root.left = new Node(50);
	tree1.root.right = new Node(300);
	tree1.root.left.left = new Node(20);
	tree1.root.left.right = new Node(70);

	/* Creating following tree as second balanced BST
				80
				/ \
			40 120
		*/

	var tree2 = new BinarySearchTree();
	tree2.root = new Node(80);
	tree2.root.left = new Node(40);
	tree2.root.right = new Node(120);

	var tree = new BinarySearchTree();
	tree.root = tree.mergeTrees(tree1.root, tree2.root);
	document.write(
	"Following is Inorder traversal of the merged tree <br>"
	);
	tree.inorder();
	
</script>
