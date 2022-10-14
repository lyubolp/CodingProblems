# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len_node = head
        
        l = 0
        while len_node is not None:
            l += 1
            len_node = len_node.next
        
        mid = l // 2
        
        if l < 2:
            return None
        
        prev, current = head, head.next
        
        for i in range(mid - 1):
            prev, current = current, current.next
            
        prev.next = current.next
        
        return head

