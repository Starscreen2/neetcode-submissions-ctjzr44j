class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        arr = nums
        result = []

        for i in range(len(nums)):
            position = i
            product = 1

            for j in range(len(nums)):
                if j != position:
                    product *= arr[j]
                
            result.append(product)

        return result




        
        
        # res = [1] * (len(nums))

        # prefix = 1
        # for i in range(len(nums)):
        #     res[i] = prefix
        #     prefix *= nums[i]
        # postfix = 1
        # for i in range(len(nums) - 1, - 1, - 1):
        #     res[i] *= postfix
        #     postfix *= nums[i]
        # return res