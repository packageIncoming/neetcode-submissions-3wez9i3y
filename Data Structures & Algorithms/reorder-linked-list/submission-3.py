# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# solution with o(n) time o(1) space

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def revStartFrom(node):
            prev=None
            cur=node
            while cur:
                nxt=cur.next
                cur.next=prev
                prev=cur
                cur=nxt
            return prev
        
        midStart = head
        fastPointer = head
        n=0
        while fastPointer and fastPointer.next:
            midStart=midStart.next
            fastPointer = fastPointer.next.next
            n+=1
        
        rHalf = revStartFrom(midStart)
        cur=head
        for _ in range(n):
            curNxt=cur.next
            rHalfNext=rHalf.next
            cur.next=rHalf
            rHalf.next=curNxt
            cur=curNxt
            rHalf=rHalfNext
        cur.next=None


        
