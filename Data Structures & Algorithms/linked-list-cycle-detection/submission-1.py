# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # if at any point .next =null then there isn't a loop
        s_ptr = head
        f_ptr = head
        while s_ptr.next is not None and f_ptr.next is not None and f_ptr.next.next is not None:
            s_ptr = s_ptr.next
            f_ptr = f_ptr.next.next
            if s_ptr == f_ptr:
                return True
        return False