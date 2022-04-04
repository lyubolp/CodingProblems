# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        values = []
        
        while head is not None:
            values.append(head.val)
            head = head.next
            
        values[k-1], values[-k] = values[-k], values[k-1]
        
        result_head = ListNode(values[0])
        result = result_head
        
        for item in values[1:]:
            result_head.next = ListNode(item)
            result_head = result_head.next
        
        return result

