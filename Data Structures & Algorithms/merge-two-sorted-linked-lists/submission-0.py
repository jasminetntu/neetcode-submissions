# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        return self.merge(list1, list2)

    def merge(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        if l1.val < l2.val:
            temp = l1.next
            l1.next = self.merge(temp, l2)
            return l1
        else:
            temp = l2.next
            l2.next = self.merge(temp, l1)
            return l2
        