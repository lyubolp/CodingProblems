# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        stack = [(root, [])]
        
        result = []
        while len(stack) > 0:
            current_root, current_path = stack.pop()
            
            if current_root is not None:
                if current_root.left is None and current_root.right is None:
                    current_path = [node.val for node in current_path] + [current_root.val]
                    if sum(current_path) == targetSum:
                        result.append(current_path)
                else:
                    stack.append((current_root.left, current_path + [current_root]))
                    stack.append((current_root.right, current_path + [current_root]))
        
        return result

