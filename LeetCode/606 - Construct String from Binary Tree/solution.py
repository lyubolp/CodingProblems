# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def string_representation(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ''
        
        center = str(root.val)
        left = '(' + self.string_representation(root.left) + ')'
        right = '(' + self.string_representation(root.right) + ')'
        
        if right == '()':
            right = ''
            if left == '()':
                left = ''
        
        return center + left + right
    
    def tree2str(self, root: Optional[TreeNode]) -> str:
        str_representation = self.string_representation(root)
        return str_representation

