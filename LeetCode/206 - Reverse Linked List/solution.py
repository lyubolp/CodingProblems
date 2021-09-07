# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        stack = []
        
        current = head
        while current is not None:
            stack.append(current.val)
            current = current.next
            
        result_head = ListNode(stack.pop())
        
        current_result = result_head
        
        while len(stack) > 0:
            current_result.next = ListNode(stack.pop())
            current_result = current_result.next
        return result_head

