class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target = math.floor(len(nums)/3)

        res=[]

        m = {}

        for num in nums:
            m[num] = m.get(num,0)+1
            if len(m.keys()) > 2:
                newDict = {}
                for n, count in m.items():
                    if count > 1:
                        newDict[n] = count-1
                m=newDict
        #print(m)
        for k in m.keys():
            if nums.count(k) > len(nums) // 3:
                res.append(k)
        return res