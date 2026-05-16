# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = list()
        dummy = ListNode()
        prev = dummy
        for i in range(len(lists)): 
            prev.next = lists[i] 
            while prev.next != None:
                prev = prev.next

        temp = dummy.next
        while temp != None:
            values.append(temp.val)
            temp = temp.next

        sorted_values = sorted(values)
        dummy1 = ListNode()
        prev1 = dummy1
        for val in sorted_values:
            new_node = ListNode(val)
            prev1.next = new_node
            prev1 = new_node
        return dummy1.next

        