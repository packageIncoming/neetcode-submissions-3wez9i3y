# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        cur = dummyHead
        while list1 and list2:
            if list1.val < list2.val:
                temp = list1.next
                cur.next = list1
                cur = cur.next
                list1 = temp
            else:
                temp = list2.next
                cur.next = list2
                cur = cur.next
                list2 = temp
        while list1:
            temp = list1.next
            cur.next = list1
            cur = cur.next
            list1 = temp
        while list2:
            temp = list2.next
            cur.next = list2
            cur = cur.next
            list2 = temp
        return dummyHead.next