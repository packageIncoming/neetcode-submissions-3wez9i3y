# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        resultHead = ListNode(0)
        prev = None
        cur = resultHead

        while l1 and l2:
            s = l1.val + l2.val
            cur.val += s
            cout = 0
            if cur.val >=10:
                cur.val -= 10
                cout = 1
            nextResult = ListNode(cout)
            cur.next = nextResult
            prev=cur
            cur = nextResult
            l1 = l1.next
            l2 = l2.next



        while l1:
            cur.val += l1.val
            cout = 0
            if cur.val >=10:
                cur.val -= 10
                cout = 1
            nextResult = ListNode(cout)
            cur.next = nextResult
            prev=cur
            cur = nextResult
            l1 = l1.next
        while l2:
            cur.val += l2.val
            cout = 0
            if cur.val >=10:
                cur.val -= 10
                cout = 1
            nextResult = ListNode(cout)
            cur.next = nextResult
            prev=cur
            cur = nextResult
            l2 = l2.next

        if not l1 and not l2 and prev.next.val == 0:
            prev.next = None  
            return resultHead
        return resultHead