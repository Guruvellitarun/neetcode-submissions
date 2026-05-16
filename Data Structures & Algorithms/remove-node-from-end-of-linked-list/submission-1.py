# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # What if i reverse the list and remove the value
        if head == None or head.next == None:
            return None

        b, c, a = None, head, head
        while c:
            a = c.next
            c.next = b
            b = c
            c = a
        
        if n == 1:
            b = b.next
        else:
            temp, prev = b, b
            while (n-1) != 0:
                prev = temp
                temp = temp.next
                n -= 1
            prev.next = temp.next

        p, c, a = None, b, b
        while c:
            a = c.next
            c.next = p
            p = c
            c = a

        return p

        