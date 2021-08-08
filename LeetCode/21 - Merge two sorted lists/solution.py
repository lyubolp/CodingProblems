# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = None
        
        if l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                root = ListNode(l1.val)
                l1 = l1.next
            else:
                root = ListNode(l2.val)
                l2 = l2.next
        elif l1 is None and l2 is not None:
            return l2
        elif l1 is not None and l2 is None:
            return l1
        else:
            return None
        
        current = root
        
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                current.next = ListNode(l1.val)
                l1 = l1.next
            else:
                current.next = ListNode(l2.val)
                l2 = l2.next
            current = current.next
        
        leftover_list = None
        if l1 is None and l2 is not None:
            leftover_list = l2
        elif l1 is not None and l2 is None:
            leftover_list = l1
        
        while leftover_list is not None:
            current.next = ListNode(leftover_list.val)
            current = current.next
            leftover_list = leftover_list.next
        
        return root
 
