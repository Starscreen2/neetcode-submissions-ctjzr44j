class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for i in s:
            if i - 1 not in s:
                y = i
                while y in s:
                    y += 1
                longest = max(longest, y - i)
        return longest