class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1, nums2 # A is shorter, B is longer
        if len(B)<len(A):
            A,B=B,A
        tot = len(A)+len(B)
        half = tot//2
        l,r = 0, len(A)-1
        while True:
            midA = (l+r)//2 
            partitionB =  half - midA - 2 # idx of up to where we get elements from B
            ALeft = A[midA] if midA >= 0 else float('-inf') # get rightmost value in left part. of A
            ARight = A[midA+1] if midA+1 < len(A) else float('inf') # get leftmost value in right part. of A
            BLeft = B[partitionB] if partitionB >= 0 else float('-inf') # get rightmost value in left part. of B
            BRight = B[partitionB+1] if partitionB+1 < len(B) else float('inf') # get leftmost value in right part. of B

            if ALeft <=BRight and BLeft <= ARight:
                # got the correct partition now figure out if odd or even case
                if tot%2:
                    # even so we need to average mins and return 
                    return  min(ARight,BRight)
                else:
                    # odd so we just return the min of the right
                    return ( max(ALeft,BLeft) + min(ARight,BRight)) / 2
            else:
                # our range is wrong
                if ALeft > BRight:
                    r=midA-1 # value was too high
                else:
                    l=midA+1 # value was too low