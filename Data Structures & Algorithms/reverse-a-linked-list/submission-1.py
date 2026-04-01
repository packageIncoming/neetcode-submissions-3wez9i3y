# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    prev = None
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Recursive solution
        #Base case: a single node is already reversed
        if head is None:
            return self.prev
        elif head.next is None:
            head.next = self.prev
            return head
        #Recursive case
        temp = head.next
        head.next = self.prev
        self.prev = head
        return self.reverseList(temp)
