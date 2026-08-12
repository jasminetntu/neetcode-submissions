# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # --- iteratively
        prev = None
        curr = head

        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

        # --- recursively
        # return self.reverse(None, head)

    # def reverse(self, prev, curr):
    #     if curr is None:
    #         return prev
        
    #     temp = curr.next
    #     curr.next = prev
    #     return self.reverse(curr, temp)