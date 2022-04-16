# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        vals = []
        
        
        while len(stack) > 0:
            node = stack.pop()
            
            if node is not None:
                vals.append(abs(node.val))
                
                stack.append(node.left)
                stack.append(node.right)
        
        vals.sort()
        result = vals[-1]
        for i in range(len(vals) - 1):
            if vals[i+1] - vals[i] < result:
                result = vals[i+1] - vals[i]
        
        return result

