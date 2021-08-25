class Solution:
    def inorderTraversalHelper(self, root: Optional[TreeNode], res: List[int]):
        if root is None:
            return
        
        self.inorderTraversalHelper(root.left, res)
        res.append(root.val)
        self.inorderTraversalHelper(root.right, res)
        
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        result = []
        
        self.inorderTraversalHelper(root, result)
        
        
        return result

