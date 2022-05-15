# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = [(root, 1)]
        
        result = {}
        while len(queue) > 0:
            current_node, current_level = queue.pop(0)
            
            if current_node is not None:
                if current_level in result:
                    result[current_level].append(current_node.val)
                else:
                    result[current_level] = [current_node.val]
                
                queue.append((current_node.left, current_level + 1))
                queue.append((current_node.right, current_level + 1))
        
        deepest_level = max(result.keys())
        return sum(result[deepest_level])

