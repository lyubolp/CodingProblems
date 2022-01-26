# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack = [root]
        result = []
        
        while len(stack) > 0:
            current = stack.pop()
            
            result.append(current.val)
            if current.left is not None:
                stack.append(current.left)
            
            if current.right is not None:
                stack.append(current.right)
        
        return result
        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        result = self.dfs(root1) + self.dfs(root2)
        result.sort()
        return result

