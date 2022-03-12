"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        nodes = {None: None}
        root = head
        
        copy_head = Node(-1)
        copy_head_2 = copy_head
        
        while root is not None:
            copy_head.next = Node(root.val, random=root.random)
            
            nodes[root] = copy_head.next
            
            copy_head = copy_head.next
            root = root.next
            
        copy_head_2 = copy_head_2.next
        result = copy_head_2
        
        
        while copy_head_2 is not None:
            copy_head_2.random = nodes[copy_head_2.random]
            copy_head_2 = copy_head_2.next
        
        return result

