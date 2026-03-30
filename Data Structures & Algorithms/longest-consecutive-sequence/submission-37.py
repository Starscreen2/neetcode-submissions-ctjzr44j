class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = sorted(nums)

        counter = 1
        largest = 1
        prev = nums[0]

        for i in nums[1:]:
            if i == prev + 1:
                counter += 1
                prev += 1
            elif i == prev:
                continue
            else:
                largest = max(largest, counter)
                counter = 1
            prev = i
        return max(largest, counter)


