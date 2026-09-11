class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) - 1
        max_water = 0

        #we are trying to store the most ammount of water
        #the shortest number is where can 

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            max_water = max(area, max_water)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_water
