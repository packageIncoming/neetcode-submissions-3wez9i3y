# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def getGCD(n1,n2):
            while n2 > 0:
                n1, n2 = n2, n1%n2
            return n1
            
        def insert(prevNode,val):
            newNode = ListNode()
            newNode.val = val
            temp = prevNode.next    
            prevNode.next = newNode
            newNode.next = temp
        
        node = head
        while node and node.next:
            nxt = node.next
            gcd = getGCD(node.val,nxt.val)
            insert(node,gcd)
            node=nxt
        
        return head
