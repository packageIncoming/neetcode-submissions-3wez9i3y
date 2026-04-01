'''
maxheap of size k
    - elements are (|a-x|,a)
    - therefore the top element is always the one that is most distant
- at the end return element[1] for element in maxheap

size complexity: O(k) 
time complexity: O(n + klogk)?
'''
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # heap 
        maxHeap = []
        for i in range(len(arr)):
            dist = abs(arr[i] - x)
            if maxHeap and len(maxHeap) == k and (dist< -maxHeap[0][0] or (dist == -maxHeap[0][0] and arr[i] < maxHeap[0][1] )):
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap,(-dist,arr[i]))
            elif len(maxHeap) < k:
                heapq.heappush(maxHeap,(-dist,arr[i]))
        return sorted([elem[1] for elem in maxHeap])