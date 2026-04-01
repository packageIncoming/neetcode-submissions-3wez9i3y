# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.val)
        secondHalfStart = slow.next
        slow.next = None

        #2. Reverse second half
        prev = None
        cur = secondHalfStart
        while cur:
            temp  =cur.next
            cur.next = prev
            prev = cur
            cur = temp
        # 3. Merge halves
        reversedPtr = prev
        originalPtr = head
        while reversedPtr:
            temp1 = originalPtr.next
            temp2 = reversedPtr.next
            originalPtr.next = reversedPtr
            reversedPtr.next = temp1
            reversedPtr = temp2
            originalPtr = temp1



