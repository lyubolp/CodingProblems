# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = {}
        
        while head is not None:
            if head.val in count:
                count[head.val] += 1
            else:
                count[head.val] = 1
            head = head.next
            
        result = ListNode(-1)
        root = result
        for key in sorted(count.keys()):
            if count[key] == 1:
                result.next = ListNode(key)
                result = result.next
        
        return root.next

