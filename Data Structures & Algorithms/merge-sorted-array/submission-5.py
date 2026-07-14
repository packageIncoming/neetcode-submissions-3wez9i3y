'''

'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a1p = m-1
        a2p = n-1
        cur = m+n-1
        while a2p>-1:
            if a1p>=0 and nums1[a1p] >= nums2[a2p]:
                nums1[cur] = nums1[a1p]
                a1p-=1
            else:
                nums1[cur] = nums2[a2p]
                a2p-=1
            cur-=1