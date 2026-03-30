class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        best = 0

        for i in prices:
            if i < lowest:
                lowest = i
            else:
                best = max(best, i - lowest)

        return best