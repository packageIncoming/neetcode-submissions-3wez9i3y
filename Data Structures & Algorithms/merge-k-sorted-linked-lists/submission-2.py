# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummyHead = ListNode()
        cur = dummyHead
        while True:
            lowestIdx = -1
            for i in range(len(lists)):
                if lists[i] == None:
                    pass
                else :
                    if (lowestIdx <0) or (lowestIdx>=0 and  lists[i].val < lists[lowestIdx].val):
                        lowestIdx = i
           # print("current lowest: ", lists[lowestIdx].val)
            if lowestIdx >= 0:
                temp = lists[lowestIdx].next
                cur.next = lists[lowestIdx]
                lists[lowestIdx] = temp
                cur = cur.next
            else:
                break


        return dummyHead.next