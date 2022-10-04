# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        stack = [(root, 0)]
        
        while len(stack) > 0:
            current_node, current_score = stack.pop()
            
            if current_node is None:
                continue
                
            if current_node.left is None and current_node.right is None and current_score + current_node.val == targetSum:
                return True
            else:
                stack.append((current_node.left, current_score + current_node.val))
                stack.append((current_node.right, current_score + current_node.val))
        
        return False

