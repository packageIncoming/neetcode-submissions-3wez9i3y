# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sorted_list_head = None
        cur = None
        i=0
        while True:
            lowest_list_idx = -1
            for  j in range(0,len(lists)):
                jth_list = lists[j]
                if jth_list is not None :
                    if lowest_list_idx == -1 or (jth_list.val < lists[lowest_list_idx].val):   
                        lowest_list_idx = j
            if lowest_list_idx == -1:
                break
            focus_list = lists[lowest_list_idx]
            temp = focus_list.next
            if cur is None:
                cur = focus_list
                if sorted_list_head is None:
                    sorted_list_head = cur
                lists[lowest_list_idx] = temp
                continue
            cur.next = focus_list
            lists[lowest_list_idx] = temp
            #print(cur.val)
            cur = cur.next


        return sorted_list_head