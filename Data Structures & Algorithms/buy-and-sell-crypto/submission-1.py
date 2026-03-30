class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        best = 0

        for i in prices:
            if i < lowest: # find the lowest
                lowest = i
            else:
                best = max(best, i - lowest) # keep comparing for the highest profit subtracted by the lowest

        return best