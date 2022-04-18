# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs_with_list(self, root: Optional[TreeNode], values: List[int]):
        if root is not None:
            self.dfs_with_list(root.left, values)
            values.append(root.val)
            self.dfs_with_list(root.right, values)
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        self.dfs_with_list(root, values)
        
        return values[k-1]

