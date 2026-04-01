from collections import deque
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        xor_tot = 0
        subs = deque()
        subs.append([])
        # this feels like overkill but I'm sure there's some mathematical solution
        # generate permutations
        for i in range(len(nums)):
            for j in range(len(subs)):
                #print(subs)
                sub = subs.popleft()
                # don't include
                subs.append(sub.copy())
                # include:
                w = sub.copy()
                w.append(nums[i])
                subs.append(w)
        for arr in subs:
            if len(arr)>0:
                tot = arr[0]
                for i in range(1,len(arr)):
                    tot = tot ^ arr[i]
                xor_tot+=tot


        return xor_tot