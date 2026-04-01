class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # bucket sort
        buckets = [0,0,0]# only 0,1,2 are available
        for num in nums:
            buckets[num]+=1
        # now add to result
        print(buckets)
        i=0
        for num in range(len(buckets)):
            print(num,buckets[num])
            for j in range(buckets[num]):
                nums[i]=num
                i+=1
