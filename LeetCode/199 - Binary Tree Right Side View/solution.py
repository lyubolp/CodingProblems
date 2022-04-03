# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = [(root, 1)]
        
        levels = {}
        
        while len(queue) > 0:
            current_node, current_level = queue.pop(0)
            
            if current_node is not None:
                if current_level not in levels:
                    levels[current_level] = [current_node.val]
                else:
                    levels[current_level].append(current_node.val)
                
                queue.append((current_node.left, current_level + 1))
                queue.append((current_node.right, current_level + 1))
        
        result = [(levels[level][-1], level) for level in levels]
        result.sort(key=lambda x: x[1])
        
        return [item[0] for item in result]

