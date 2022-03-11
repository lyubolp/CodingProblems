# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or head is None:
            return head
        
        l = 0
        count = head
        while count is not None:
            l += 1
            count = count.next
        
        if l == 1:
            return head
        
        k = k % l
        if k == 0:
            return head 
        
        original_head = head
        
        for i in range(l - k - 1):
            head = head.next
        
        new_root = head.next
        head.next = None
        result = new_root
        
        for i in range(k - 1):
            new_root = new_root.next
        
        new_root.next = original_head
        
        return result

