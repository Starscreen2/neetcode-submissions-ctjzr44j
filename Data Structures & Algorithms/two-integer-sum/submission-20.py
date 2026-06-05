class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashh = {}

        # temp other_num, 
        for i, num in enumerate(nums):
            other_num = target - nums[i]
            if other_num in hashh:
                return [hashh[other_num], i]

            hashh[num] = i