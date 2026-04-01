class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_buckets= defaultdict(set)
        freqs= defaultdict(int)
        highest_freq=0
        for num in nums:
            freqs[num]+=1
            highest_freq=max(highest_freq,freqs[num])
            if freqs[num]==1:
                # just added
                freq_buckets[freqs[num]].add(num)
            else:
                # old, remove from previous bucket and move up one
                freq_buckets[freqs[num]-1].remove(num)
                freq_buckets[freqs[num]].add(num)
        
        top = []
        for i in range(highest_freq,-1,-1):
            bucket = freq_buckets[i]
            for num in bucket:
                top.append(num)
                if len(top)==k:
                    return top
        return top