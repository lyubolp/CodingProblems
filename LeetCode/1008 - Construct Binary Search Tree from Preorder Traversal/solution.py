# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insert(self, root: TreeNode, value: int):
        if value <= root.val:
            if root.left == None:
                root.left = TreeNode(value)
            else:
                self.insert(root.left, value)
        else:
            if root.right == None:
                root.right = TreeNode(value)
            else:
                self.insert(root.right, value)
        
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder.pop(0))
        
        for num in preorder:
            self.insert(root, num)
            
        return root

