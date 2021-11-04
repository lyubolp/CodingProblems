# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        stack = [(root, False)]
        
        result = []
        while len(stack) > 0:
            current_node, is_left = stack.pop()
            
            if is_left and current_node.left is None and current_node.right is None:
                result.append(current_node.val)
                
            if current_node.left is not None:
                stack.append((current_node.left, True))
                
            if current_node.right is not None:
                stack.append((current_node.right, False))
                
        
        return sum(result)

