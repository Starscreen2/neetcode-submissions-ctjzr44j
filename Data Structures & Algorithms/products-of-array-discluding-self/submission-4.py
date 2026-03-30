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

