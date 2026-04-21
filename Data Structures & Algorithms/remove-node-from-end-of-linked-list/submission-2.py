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
        if not head.next:
            # only one node so just return nothing
            return None
        def reverse(node):
            prev=None
            cur=node
            while cur:
                temp = cur.next
                cur.next=  prev
                prev=cur
                cur=temp
            return prev
        
        tail = reverse(head)
        if n == 1:
            return reverse(tail.next)
        prev=None
        cur=tail
        for i in range(n-1):
            prev=cur
            cur=cur.next
        if prev:
            prev.next = cur.next
        return reverse(tail)
