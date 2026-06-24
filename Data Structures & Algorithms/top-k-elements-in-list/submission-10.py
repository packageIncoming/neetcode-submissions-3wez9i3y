'''
obvious solution:
freq dict O(n)-> heap or sort O(nlogn)-> get top k O(1)

The bottleneck is the o(nlogn)

is there a way to bring it down to o(n)

o(n) means you get a single pass


one way would be to do two linear passes

first pass:
    update frequency
    have another dictionary of [freq]:[set of numbers]
    move up whenever number is seen
    update max frequency
second pass:
    from max frequency down to 0:
        grab elements from that set
        once our res has k elements we return

answer guaranteed to be unique so no 2 numbers at k=1 for instance

'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq= {}
        freq_buckets=defaultdict(set)
        mf=0

        for num in nums:
            p = freq.get(num,0)
            freq[num] = freq.get(num,0)+1
            if p > 0:
                freq_buckets[p].remove(num)
            freq_buckets[freq[num]].add(num)
            mf = max(mf,freq[num])

        res=[]

        for bucket in range(mf,-1,-1):
            s = freq_buckets[bucket]
            for num in s:
                res.append(num)
                if len(res) == k:
                    return res


        