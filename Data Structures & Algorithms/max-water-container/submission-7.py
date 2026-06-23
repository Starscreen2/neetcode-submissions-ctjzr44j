class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        temp_total = 0
        while l < r:
            # width = r - l
            lowest = min(heights[l], heights[r])
            temp_total = max((r - l) * lowest, temp_total)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return temp_total
