class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # naive solution (with division): get the array product,
        #then at each element divide the product by that element (if its not 0)
        array_product= nums[0]
        zero_idxs = []
        for i in range(1,len(nums)):
            num = nums[i]
            if num != 0:
                array_product *= num
            else:
                zero_idxs.append(i)
        products = []
        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                if len(zero_idxs) > 1:
                    products.append(0)
                else:
                    products.append(array_product)
            else:
                if len(zero_idxs) > 0:
                    products.append(0)
                else:
                    products.append(int(array_product / num))
        return products