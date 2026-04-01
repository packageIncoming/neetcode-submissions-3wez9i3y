class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1. turn into freq set
        freq = defaultdict(int)
        buckets = [[] for _ in range(len(nums)+1)]

        for num in nums:
            freq[num]+=1
        for num in freq:
            count = freq[num]
            buckets[count].append(num)
        most_freq = []
        for i in range(len(buckets)-1,0,-1):
            for j in buckets[i]:
                most_freq.append(j)
                if len(most_freq)== k:
                    return most_freq
        