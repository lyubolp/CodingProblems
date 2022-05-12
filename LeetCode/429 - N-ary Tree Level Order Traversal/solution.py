"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        queue = [(root, 0)]
        result = {}
        
        while len(queue) > 0:
            current_node, current_level = queue.pop(0)
            
            if current_node != None:
                if current_level not in result:
                    result[current_level] = [current_node.val]
                else:
                    result[current_level].append(current_node.val)
                
                
                for child in current_node.children:
                    queue.append((child, current_level + 1))
        
        return [result[key] for key in result]

