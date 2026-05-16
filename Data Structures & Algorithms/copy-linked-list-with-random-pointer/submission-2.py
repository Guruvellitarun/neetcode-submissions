"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        # There is a 3 Way approch for this problem
        # 1. Create the node in interlavent of the current node
        curr = head
        while curr:
            newnode = Node(curr.val)
            newnode.next = curr.next
            curr.next = newnode
            curr = newnode.next
        
        # 2. Now add the random to this linked list
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # 3. Now remove the new list for the old.
        copy_head = head.next
        curr = head
        while curr:
            copy = curr.next
            curr.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            curr = curr.next
        
        return copy_head
