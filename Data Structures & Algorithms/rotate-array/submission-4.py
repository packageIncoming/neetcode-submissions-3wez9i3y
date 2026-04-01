'''
* New position is (index+k)% len(arr)

O(n) time complexity 
solution would be to instantiate new empty array then fill accordingly
then replace values in nums based on that 

k % len(arr) is the actual displacement within the array for each element



'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverseSection(arr,i,j):
            while i < j:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
                i+=1
                j-=1
        k=k%len(nums)
        reverseSection(nums,0,len(nums)-1)
        reverseSection(nums,0,k-1)
        reverseSection(nums,k,len(nums)-1)

