class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            other_number = target - nums[i]
            if other_number in hashmap:
                return [hashmap[other_number], i]
            hashmap[nums[i]] = i
