'''
Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.
    - Minheap to track k elements, pop top element to get kth largest
By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.
    - Duplicates should not be an issue 

Follow-up: Can you solve it without sorting?
    - Minheap allows for not having to sort so no need to make additional solution
'''


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.heap = []
        for i in range(len(nums)):
            heapq.heappush(self.heap,nums[i])
            if len(self.heap)>k:
                heapq.heappop(self.heap)
        return self.heap[0]