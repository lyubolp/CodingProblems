# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        stack = [head]
        visited = set()
        while len(stack) > 0:
            current_node = stack.pop()
            
            if current_node in visited:
                return current_node
            
            visited.add(current_node)
            
            if current_node.next is not None:
                stack.append(current_node.next)
                
        return None
 
