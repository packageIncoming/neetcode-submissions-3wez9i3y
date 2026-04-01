class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # solution idea: make the freq map and then get the k most frequent elements
        h = {}
        for num in nums:
            h[num] = h.get(num,0)+1
        top_k = []
        h = sorted(h.items(), key = lambda item: item[1],reverse=True)
        return [item[0] for item in h[:k]]