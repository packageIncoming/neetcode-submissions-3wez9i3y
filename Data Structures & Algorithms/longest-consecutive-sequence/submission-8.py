'''
goal: get length of longest consecutive sequence
    consecutive: for an element n, there is element n-1
    they don't have to be consecutive in the original array
        So they just have to exist is all
Naive solution would be to sort then run a sort of Kadane's algo
But you don't actually have to have them sorted, just have them 
exist

Kind of like a DP problem:
    For element i, it's 'value' ie the LCSequence that ends
    at that element i is either 0 OR 1+hashmap[i-1]

The issue with the hashmap is where do you know where to begin/end?
Can just keep track of min and max, but
worst case is you have 0, 10^9 only and you're iterating
over 10^9-2 empty space

How about going backwards?
    value of hashmap[i] is the length of sequence starting at i
    value of hashmap[i-1] = 1 + hashmap[i]
You still run into the problme of "where do I start off from next"
    10^9, check if 10^9-1 is there, ... check if 0 is there

Binary search = nlogn so no
Heaps = nlogn so no

Duplicates don't count towards length


'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hmap = {}
        longest=1
        if len(nums)==0: return 0
        high = nums[0]
        low = nums[0]
        for n in nums:
            hmap[n] = 1
            low = min(low,n)
            high = max(high,n)

        for i in range(high,low-1,-1):
            if i not in hmap: continue
            if (i-1) in hmap:
                hmap[i-1] = hmap[i]+1
                longest = max(hmap[i-1],longest)
        return longest

        
