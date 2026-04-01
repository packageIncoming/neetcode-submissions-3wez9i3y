# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        l1_ptr = list1
        l2_ptr = list2
        while l1_ptr and l2_ptr:
            if l1_ptr.val < l2_ptr.val:
                temp = l1_ptr.next
                cur.next = l1_ptr
                l1_ptr = temp
                cur = cur.next
            elif l2_ptr.val < l1_ptr.val:
                temp = l2_ptr.next
                cur.next = l2_ptr
                l2_ptr = temp
                cur = cur.next
            else:
                temp1  =l1_ptr.next
                temp2 = l2_ptr.next
                cur.next = l1_ptr
                cur.next.next = l2_ptr
                l1_ptr = temp1
                l2_ptr = temp2
                cur = cur.next.next
        #print(l1_ptr.val if l1_ptr else None,l2_ptr.val if l2_ptr else None)
        if l1_ptr:
            cur.next = l1_ptr
        elif l2_ptr:
            cur.next = l2_ptr
        return dummy.next