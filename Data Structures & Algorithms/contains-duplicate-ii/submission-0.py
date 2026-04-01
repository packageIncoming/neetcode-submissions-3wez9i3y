class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # sliding window o(n) time o(k) space complexity
        window = set()
        l=0
        for i in range(len(nums)):
            if len(window) > k:
                # need to remove before adding
                window.remove(nums[l])
                l+=1
            if nums[i] in window:
                return True
            window.add(nums[i])
        return False