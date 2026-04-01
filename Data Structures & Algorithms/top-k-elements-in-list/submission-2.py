class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1. turn into freq set
        freq = defaultdict(int)
        for num in nums:
            freq[num]+=1
        
        top_k = []
        
        for num in freq:
            if len(top_k) < k:
                top_k.append((num,freq[num]))
            else:
                lowest_idx = 0
                for i, pair in enumerate(top_k):
                    if pair[1] < top_k[lowest_idx][1]:
                        lowest_idx = i
                if freq[num] > top_k[lowest_idx][1]:
                    top_k[lowest_idx] = (num,freq[num])
        return [pair[0] for pair in top_k]