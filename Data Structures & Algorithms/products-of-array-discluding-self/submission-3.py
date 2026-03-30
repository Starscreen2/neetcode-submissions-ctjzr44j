class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = nums
        result = []


        for i in range(len(nums)):
            position = i
            digit = 1
            for j in range(len(nums)):
                if j != position:
                    digit *= arr[j]

            result.append(digit)
        return result