# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        tree = {}
        stack = [(root, 0, None)] # (Node, depth, parent)
        
        while len(stack) > 0:
            current_node, current_depth, current_parent = stack.pop()
            
            tree[current_node.val] = (current_depth, current_parent)
            
            if current_node.left != None:
                stack.append((current_node.left, current_depth + 1, current_node.val))
            
            if current_node.right != None:
                stack.append((current_node.right, current_depth + 1, current_node.val))
                
        return tree[x][0] == tree[y][0] and tree[x][1] != tree[y][1]

