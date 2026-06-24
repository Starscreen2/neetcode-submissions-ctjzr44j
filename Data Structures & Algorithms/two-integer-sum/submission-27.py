class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, num in enumerate(nums):
            other_number = target - num
            if other_number in seen:
                return [seen[other_number], index]
            seen[num] = index
