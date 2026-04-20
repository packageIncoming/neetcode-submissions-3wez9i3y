# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# brute force solution with o(n) time and o(n) space:

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n =[]
        cur = head
        while cur :
            n.append(cur)
            cur=cur.next
        
        print(n)
        
        l,r = 0, len(n)-1
        print(l,r)
        i=0
        while l < r:
            print(l,r)
            i+=1
            n[l].next = n[r]
            l+=1
            if l==r:
                break

            n[r].next = n[l]
            r-=1
        n[l].next=None
