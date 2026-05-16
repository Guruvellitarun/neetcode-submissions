# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # we are checking weather there are k Node in the linkedlist
        curr = head
        for _ in range(k):
            if not curr:
                return head
            curr = curr.next
        
        prev, curr = None, head
        for _ in range(k):
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        head.next = self.reverseKGroup(curr, k)

        return prev
