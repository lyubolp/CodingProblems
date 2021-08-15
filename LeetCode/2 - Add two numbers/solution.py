# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(l1.val + l2.val)
        root = result
        additional = 0
        
        if result.val >= 10:
            result.val -= 10
            additional = 1
        
        l1 = l1.next
        l2 = l2.next
        
        
        while l1 is not None and l2 is not None:
            next_node = ListNode(l1.val + l2.val + additional)
            
            if additional == 1:
                additional = 0
                
            if next_node.val >= 10:
                next_node.val -= 10
                additional = 1
            
            result.next = next_node
            result = result.next
            l1 = l1.next
            l2 = l2.next
        
        
        
        while l1 is not None:
            next_node = ListNode(l1.val + additional)
            
            if additional == 1:
                additional = 0
                
            if next_node.val >= 10:
                next_node.val -= 10
                additional = 1
            result.next = next_node
            result = result.next
            l1 = l1.next
            
        while l2 is not None:
            next_node = ListNode(l2.val + additional)
            
            if additional == 1:
                additional = 0
                
            if next_node.val >= 10:
                next_node.val -= 10
                additional = 1
            result.next = next_node
            result = result.next
            l2 = l2.next
        
        if additional == 1:
            result.next = ListNode(1)
        return root

