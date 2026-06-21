class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r=len(nums)-1

        k=0

        for l in range(len(nums)):
            if nums[l] != val:
                k+=1
            else:
                while r>-1 and nums[r] == val:
                    r-=1
                if l >= r: break
                nums[l],nums[r] = nums[r],nums[l]
                k+=1


        return k