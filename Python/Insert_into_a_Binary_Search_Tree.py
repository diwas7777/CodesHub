# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # If the root is None, create a new node with the given value
        if not root:
            return TreeNode(val)
        
        # If the value is less than the root, insert it into the left subtree
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        
        # If the value is greater than or equal to the root, insert it into the right subtree
        else:
            root.right = self.insertIntoBST(root.right, val)
            
        # Return the root node after insertion
        return root
    
# Sample usage
if __name__ == '__main__':
    # Create a binary search tree with root value 4
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    
    # Insert value 5 into the binary search tree
    sol = Solution()
    root = sol.insertIntoBST(root, 5)
    
    # Traverse the binary search tree using in-order traversal
    def inorderTraversal(root):
        if root:
            inorderTraversal(root.left)
            print(root.val)
            inorderTraversal(root.right)
    inorderTraversal(root)
