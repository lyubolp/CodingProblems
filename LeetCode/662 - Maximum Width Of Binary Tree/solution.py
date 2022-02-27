# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = [(root, 1, 1)]
        
        result = 0
        levels = {}
        while len(queue) > 0:
            current_node, current_level, current_width = queue.pop()
            
            if current_node is not None:
                if current_level in levels:
                    levels[current_level].append(current_width)
                else:
                    levels[current_level] = [current_width]
                    
                queue.append((current_node.left, current_level + 1, 2 * current_width - 1))
                queue.append((current_node.right, current_level + 1, 2 * current_width))
            
        
        widths = [max(levels[key]) - min(levels[key]) + 1 for key in levels]
        return max(widths)

