# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.first = None
        self.second = None
        self.prev = TreeNode(-sys.maxsize)
        
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.dfs(root)
        
        self.first.val, self.second.val = self.second.val, self.first.val
        
    def dfs(self, root: Optional[TreeNode]):    
        if root is not None:
            self.dfs(root.left)
            
            if self.first is None and self.prev.val >= root.val:
                self.first = self.prev
            
            if self.first is not None and self.prev.val >= root.val:
                self.second = root
            
            self.prev = root
            
            self.dfs(root.right)

