# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseSection(self,nodeStart,nodeEnd):
        #print(f"Reversing from {nodeStart.val} to {nodeEnd.val} exclusive")
        prev = None
        cur = nodeStart
        while cur and cur != nodeEnd:
            temp = cur.next
            cur.next = prev
            prev=cur
            cur=temp
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        newHead = None
        i = 0

        cur = head
        lastLeftOff = head
        lastChunkEnd = None
        while cur:
            i+=1
            if i == k:
                temp  = cur.next
                #print(f"Reversing from {lastLeftOff.val} to {cur.val}")
                newGroupStart = self.reverseSection(lastLeftOff,cur.next)
                print(lastLeftOff.val)
                if lastChunkEnd is not None:
                    #print(f"Appending to previous chunk that ended in {lastChunkEnd.val}")
                    lastChunkEnd.next = newGroupStart
                lastChunkEnd = lastLeftOff
                if newHead is None:
                    newHead = newGroupStart
                cur = temp
                lastLeftOff = cur
                i=0

            else:
                cur=cur.next
        if lastLeftOff:
            #print(lastChunkEnd.val)
            cur = lastChunkEnd
            while lastLeftOff:
                temp  =lastLeftOff.next
                cur.next = lastLeftOff
                cur = lastLeftOff
                lastLeftOff=temp
        return newHead