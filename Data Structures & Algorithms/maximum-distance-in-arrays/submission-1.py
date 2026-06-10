'''
Arrays are sorted in ascending order
    for each array, arr[0]=min of arr, arr[-1] = max of arr

Goal is to get the maximum distance

If I had a SINGLE sorted array & I wanted the distance, I'd 
do arr[-1]-arr[0]

I think middle values are irrelevant here?

What does the brute force solution look like?
Get the min and max of all arrays & calculate the biggest difference
with every other array
Input: arrays = [[1,2,3],[4,5],[1,2,3]]
-> (1,3), (4,5), (1,3)
    -> (1,3)'s maximum differences:
        If we choose to go with 1 it's 4 (5-1)
        If we choose to go with 3 it's 2 (5-3)
    -> (4,5)'s MD:
        4->3
        5->4
    -> (1,3)'s MD: above
Keep a running track of the global MD
For m arrays you compare against m-1 arrays
    -> O(n^2) time complexity O(1) space

But is there a way to do a single pass?
Torn between this being greedy or DP
Are there subproblems in this?

I think the problem comes down to knowing whether to
select an array based on its minimum or its maximum value
the thing is that adding a new array to the mix might make a previous
best decision not so good

if you have [4,5] and [1,2,3]


What is my thought process RN?
The BF solution would be to compare every array against every other array

2 pointers/queues????

Almost like container with the most water?
'''


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        lowQ = []
        highQ = []
        for i in range(len(arrays)):
            arr = arrays[i]
            lowQ.append((arr[0],i))
            highQ.append((arr[-1],i))
        
        lowQ.sort()
        highQ.sort(reverse=True)
        

        lItem = lowQ[0]
        hItem = highQ[0]
        if lItem[1] != hItem[1]:
            return abs(lItem[0] - hItem[0])
        else:
            if len(lItem)<1: return 0
            lInRes = (
                abs(
                    lowQ[1][0]- hItem[0]
                )
            )
            rInRes = (
                abs(
                    lItem[0] - highQ[1][0]
                )
            )
            return max(lInRes,rInRes)


