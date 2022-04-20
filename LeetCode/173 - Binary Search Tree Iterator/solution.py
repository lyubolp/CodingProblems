# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = []
        self.dfs(root)
        
        self.index = 0
        
        
    def dfs(self, root: Optional[TreeNode]):
        if root is not None:
            self.dfs(root.left)
            self.nodes.append(root)
            self.dfs(root.right)
            
    def next(self) -> int:
        self.index += 1
        return self.nodes[self.index - 1].val

    def hasNext(self) -> bool:
        return self.index < len(self.nodes)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
