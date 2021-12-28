# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        
        len_head = head
        
        while len_head is not None:
            length += 1
            len_head = len_head.next
            
        target = length // 2
        
        for i in range(target):
            head = head.next    
        
        return head

