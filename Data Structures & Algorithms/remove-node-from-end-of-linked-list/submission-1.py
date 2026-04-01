# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # edge case: head node only so just return nothing
        if not head.next:
            return None
        #Reverse->Remove->Reverse
        #1. reverse LL
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur=nxt
        #prev now points to head of reversed list
        #2. Remove nth node
        i=1
        prev2 = None
        cur2 = prev
        while i != n:
            prev2=cur2
            cur2=cur2.next
            i+=1
        # cur2 now points to the node to be removed
        if prev2:        
            prev2.next = cur2.next
        else:
            prev = prev.next
        del cur2
        # 3. Reverse once again
        # (recall that prev points to the head of the reversed list)
        prev3 = None
        cur3= prev
        while cur3:
            nxt = cur3.next
            cur3.next = prev3
            prev3 = cur3
            cur3 = nxt
        return prev3