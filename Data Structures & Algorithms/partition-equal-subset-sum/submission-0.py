class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        partitions = []
        def generatePartitions(cur,i):
            nonlocal partitions
            if i == len(nums) and len(cur) == len(nums):
                partitions.append(cur)
                return
            # with current
            generatePartitions(cur + "1",i+1)
            # without current
            generatePartitions(cur+"0",i+1)
        generatePartitions("",0)
        for partition in partitions:
            sum1 = 0
            sum2 = 0
            for i in range(len(partition)):
                c = partition[i]
                if c == '1':
                    sum1 += nums[i]
                else:
                    sum2 += nums[i]
            if sum1 == sum2:
                return True
        return False