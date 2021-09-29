# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self, head: Optional[ListNode]) -> int:
        if head is not None:
            return self.length(head.next) + 1
        else:
            return 0
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = self.length(head)
        
        element_count = n // k
        amount_of_bonus_nodes = n % k
        
        result = []
        prev = None
        while head is not None:
            result.append(head)
            amount_of_elements = element_count
            
            if len(result) <= amount_of_bonus_nodes:
                amount_of_elements += 1

            for i in range(amount_of_elements):
                prev = head
                head = head.next
            
            prev.next = None
        
        if len(result) < k:
            for i in range(k - len(result)):
                result.append(None)
                
        return result

