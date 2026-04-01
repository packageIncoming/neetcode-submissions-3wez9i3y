class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        n1Ptr= m-1
        n2Ptr = len(nums2)-1

        i = len(nums1)-1

        while n1Ptr > -1 and n2Ptr > -1:
            if nums1[n1Ptr] >= nums2[n2Ptr]:
                nums1[i] = nums1[n1Ptr]
                n1Ptr-=1
                i-=1
            else:
                nums1[i] = nums2[n2Ptr]
                n2Ptr-=1
                i-=1
        while n1Ptr > -1:
            nums1[i] = nums1[n1Ptr]
            n1Ptr-=1
            i-=1
        while n2Ptr > -1:
            nums1[i] = nums2[n2Ptr]
            n2Ptr-=1
            i-=1
