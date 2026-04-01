# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: return head # no change
        
        prev=None
        cur=head

        i=1
        while i < left:
            prev=cur
            cur=cur.next
            i+=1
        nodeBeforeLeft = prev
        leftNode = cur
        
        prev=None
        cur=leftNode
        for i in range(right-left+1):
            print(cur.val)
            temp = cur.next
            cur.next = prev
            prev=cur
            cur=temp
        leftNode.next = cur
        if nodeBeforeLeft:
            nodeBeforeLeft.next=prev
            return head
        else:
            return prev

