# Python3 program to check foldable binary tree

# A binary tree node has data,
# pointer to left child and a
# pointer to right child


class newNode:
	def __init__(self, d):
		self.data = d
		self.left = None
		self.right = None

# Returns true if the given
# tree is foldable


def isFoldable(node):

	# base case
	if node == None:
		return true

	# convert left subtree to its mirror
	mirror(node.left)

	# Compare the structures of the right subtree and mirrored
	# left subtree
	res = isStructSame(node.left, node.right)

	# Get the original tree back
	mirror(node.left)

	return res


def isStructSame(a, b):

	if a == None and b == None:
		return True
	if a != None and b != None and isStructSame(a.left, b.left) and isStructSame(a.right, b.right):
		return True

	return False


def mirror(node):

	if node == None:
		return
	else:

		# do the subtrees
		mirror(node.left)
		mirror(node.right)

		# swap the pointers in this node
		temp = node.left
		node.left = node.right
		node.right = temp


# Driver Code
if __name__ == '__main__':

	'''
	The constructed binary tree is
			1
		/ \
		2	 3
		\ /
			4 5
	'''
	root = newNode(1)
	root.left = newNode(2)
	root.right = newNode(3)
	root.right.left = newNode(4)
	root.left.right = newNode(5)

	if isFoldable(root):
		print("tree is foldable")
	else:
		print("Tree is not foldable")
