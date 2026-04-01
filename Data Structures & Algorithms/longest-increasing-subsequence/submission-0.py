class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [1]*len(nums)
        highest = 1
        for i in range(len(nums),-1,-1):
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    #greater value
                    memo[i] = max(memo[i],1+memo[j])
                    highest = max(highest,memo[i])
        #print(memo)
        return highest