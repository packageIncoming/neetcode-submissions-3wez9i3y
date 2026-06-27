class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)//3
        res=[]
        freq={}
        for i in range(len(nums)):
            num = nums[i]
            freq[num] = freq.get(num,0)+1
            if freq[num] > n and num not in res:
                res.append(num)
            if len(res) == 3:
                break
        return res