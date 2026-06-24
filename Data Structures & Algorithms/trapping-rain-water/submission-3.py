class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = []
        maxR = []
        minn = []
        ans = 0

        max_num_l = 0
        for l in range(len(height)):
            max_num_l = max(height[l], max_num_l)
            maxL.append(max_num_l)

        max_num_r = 0
        for r in range(len(height)-1, -1, -1):
            max_num_r = max(height[r], max_num_r)
            maxR.append(max_num_r)

        right = maxR[::-1]
        left = maxL
        for i in range(len(height)):
            minn.append(min(left[i], right[i]))

        for j in range(len(minn)):
            temp = minn[j] - height[j]
            if temp >= 0:
                ans += (minn[j] - height[j])
        return ans

