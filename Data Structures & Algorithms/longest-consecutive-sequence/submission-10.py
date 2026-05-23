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
        longest=0
        s = set(nums)
        for n in s:
            if n-1 not in s:
                cur=1
                while n+1 in s:
                    n+=1
                    cur+=1
                longest = max(cur,longest)
        return longest

        
