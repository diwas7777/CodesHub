// Java program to check foldable binary tree

/* A binary tree node has data, pointer to left child
and a pointer to right child */
class Node {
	int data;
	Node left, right;

	Node(int item)
	{
		data = item;
		left = right = null;
	}
}

class BinaryTree {
	Node root;

	/* Returns true if the given tree is foldable */
	boolean isFoldable(Node node)
	{
		boolean res;

		/* base case */
		if (node == null)
			return true;

		/* convert left subtree to its mirror */
		mirror(node.left);

		/* Compare the structures of the right subtree and
		mirrored left subtree */
		res = isStructSame(node.left, node.right);

		/* Get the original tree back */
		mirror(node.left);

		return res;
	}

	boolean isStructSame(Node a, Node b)
	{
		if (a == null && b == null)
			return true;
		if (a != null && b != null
			&& isStructSame(a.left, b.left)
			&& isStructSame(a.right, b.right))
			return true;

		return false;
	}

	/* UTILITY FUNCTIONS */

	/* Change a tree so that the roles of the left and
	right pointers are swapped at every node.
	See https:// www.geeksforgeeks.org/?p=662 for details
	*/
	void mirror(Node node)
	{
		if (node == null)
			return;
		else {
			Node temp;

			/* do the subtrees */
			mirror(node.left);
			mirror(node.right);

			/* swap the pointers in this node */
			temp = node.left;
			node.left = node.right;
			node.right = temp;
		}
	}

	/* Driver program to test above functions */
	public static void main(String args[])
	{
		BinaryTree tree = new BinaryTree();

		/* The constructed binary tree is
			1
		/ \
		2	 3
		\ /
			4 5
		*/
		tree.root = new Node(1);
		tree.root.left = new Node(2);
		tree.root.right = new Node(3);
		tree.root.right.left = new Node(4);
		tree.root.left.right = new Node(5);

		if (tree.isFoldable(tree.root))
			System.out.println("tree is foldable");
		else
			System.out.println("Tree is not foldable");
	}
}

// This code has been contributed by Mayank Jaiswal
