'''
first instinct is cycle sort here
[1000,2,4,-3] k=2

1000 moves to 4's spot, 4 moves to 1000's spot
2 moves to -3's spot, -3 moves to 2's spot
[4,-3,1000,2]
interesting note: k=2, moved 2 elements

[1,2,3,4,5,6,7,8] k =4
1 moves to 5's spot
5 moves to 1's spot
2 moves to 6's spot, 6 moves to 2's spot

what if k=3?
1 moves to 4, 4 moves to 7, 7 moves to 2, 2 moves to 5, 5 moves to 8, 8 moves to 3,
3 moves to 6, 6 moves to 1 STOP

If you were able to track what has already been moved then you could just iterate
over the whole array, that becomes o(n) space o(n) time

but we want an o(1) space solution, so make the changes in-place

the easiest o(n) solution would be to go over with a hashmap but thats o(n) time and space

k can also be very large (100k) so wouldn't want to do iteration over it



'''


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hmap = {}
        n=len(nums)
        for i in range(len(nums)):
            hmap[(i+k)%n] = nums[i]
        for i in range(len(nums)):
            nums[i] = hmap[i]
            

        