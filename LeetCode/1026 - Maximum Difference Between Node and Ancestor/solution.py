# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMaxDiff(self, values: List[int]) -> int:
        return max(values) - min(values) if len(values) > 0 else 0
    def maxAncestorDiffHelper(self, root: Optional[TreeNode], visited_so_far: List[int]):
        if root is None:
            return self.getMaxDiff(visited_so_far)
        
        m1 = self.maxAncestorDiffHelper(root.left, visited_so_far + [root.val])
        m2 = self.maxAncestorDiffHelper(root.right, visited_so_far + [root.val])
        
        return max(m1, m2)
            
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.maxAncestorDiffHelper(root, [])

