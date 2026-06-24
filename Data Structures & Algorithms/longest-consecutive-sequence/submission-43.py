class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for i in s:
            if i - 1 not in s:
                min_value = i
                while min_value in s:
                    min_value += 1
                longest = max(longest, min_value - i)
        
        return longest

        