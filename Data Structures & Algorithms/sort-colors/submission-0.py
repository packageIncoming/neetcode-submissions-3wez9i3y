class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        vals = [0,0,0] # 0, 1, 2 respectively
        for i in nums:
            vals[i] +=1
        
        i=0
        for bucket in range(len(vals)):
            bucket_size = vals[bucket]
            for _ in range(bucket_size):
                nums[i] = bucket
                i+=1
