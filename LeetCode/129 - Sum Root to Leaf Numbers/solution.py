# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        stack = [(root, 0)]
        
        result = []
        while len(stack) > 0:
            current_node, current_number = stack.pop()
            
            next_number = current_number * 10 + current_node.val
            if current_node.left is None and current_node.right is None:
                result.append(next_number)
            elif current_node.left is None and current_node.right is not None:
                stack.append((current_node.right, next_number))
            elif current_node.left is not None and current_node.right is None:
                stack.append((current_node.left, next_number))
            else:
                stack.append((current_node.left, next_number))
                stack.append((current_node.right, next_number))
                
        return sum(result)

