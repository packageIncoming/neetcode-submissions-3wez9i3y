class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prefix_product = [0] * len(nums)
        right_prefix_product = [0] * len(nums)
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
            left_prefix_product[i] = prod
        prod = 1
        for i in range(len(nums)-1,-1,-1):
            prod *= nums[i]
            right_prefix_product[i] = prod
        prod_except_elem = []
        for i in range(len(nums)):
            # Handle edge cases: i==0 [first item] or i == len(nums)-1 [final item]
            if i ==0:
                prod_except_elem.append(right_prefix_product[1])
            elif i == len(nums)-1:
                prod_except_elem.append(left_prefix_product[-2])
            else:
                prod_except_elem.append(left_prefix_product[i-1] * right_prefix_product[i+1])
        return prod_except_elem