# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
goal: remove nth node from end of list (1-indexed)
[1,2,3,4] n=2 -> [1,2,4]

idea: reverse, remove, reverse
[1,2,3,4]->[4,3,2,1], count down then find and then remove and then reverse
'''

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointers method
        dummy = ListNode(val=0,next=head)
        left=dummy
        right=head

        for i in range(n):
            right=right.next
        
        while right:
            left=left.next
            right=right.next
        left.next = left.next.next
        return dummy.next

