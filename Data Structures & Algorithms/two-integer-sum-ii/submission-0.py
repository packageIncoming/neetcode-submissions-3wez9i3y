class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two pointers solution: one on left, one on right;
        #   incrementing the left pointer increases the sum,
        #   decrementing the right pointer decreases the sum,
        #   traverse towards middle to find the indices that add up to target
        #   we are guaranteed a SINGLE solution
        current_sum = numbers[0] + numbers[-1]
        l_ptr = 0
        r_ptr = len(numbers)-1
        while current_sum != target:
            while current_sum < target:
                l_ptr+=1
                current_sum = numbers[l_ptr] + numbers[r_ptr]
            while current_sum > target:
                r_ptr -=1
                current_sum = numbers[l_ptr] + numbers[r_ptr]
        return [l_ptr+1,r_ptr+1]