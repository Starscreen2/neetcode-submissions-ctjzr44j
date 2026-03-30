class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        arr = nums
        result = []

        for i in range(len(nums)):
            position = i
            mult = 1
            for j in range(len(nums)):
                if j != position:
                    mult *= arr[j]
            result.append(mult)

        return result