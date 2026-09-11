class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxL = []
        maxR = []
        # minLR = []

        reverse = height[::-1]

        max_h = 0
        for i in height:
            max_h = max(max_h, i)
            maxL.append(max_h)

        max_h = 0
        for j in reverse:
            max_h = max(max_h, j)
            maxR.append(max_h)

        # for k in range(len(height)):
        #     minLR.append()
        maxR.reverse()

        final = 0

        for num in range(len(height)):
            if min(maxL[num], maxR[num]) - height[num] <= 0:
                final += 0
            else:
                final += (min(maxL[num], maxR[num]) - height[num])

        return final

