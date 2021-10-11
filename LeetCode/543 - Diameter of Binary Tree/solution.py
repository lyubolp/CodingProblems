# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def max_path(self, root: Optional[TreeNode], current_depth) -> int:
        if root is None:
            return current_depth
        
        left = self.max_path(root.left, current_depth + 1)
        right = self.max_path(root.right, current_depth + 1)
        
        return max(left, right)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        root_depth = self.max_path(root.left, 0) + self.max_path(root.right, 0)
        left = self.diameterOfBinaryTree(root.left) if root.left is not None else 0
        right = self.diameterOfBinaryTree(root.right) if root.right is not None else 0
        
        return max(root_depth, left, right)

