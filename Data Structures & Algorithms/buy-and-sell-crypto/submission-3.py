class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowest = prices[0]
        highest_profit = 0

        for i in prices:
            difference = 0
            highest_profit = max(i - lowest, highest_profit)
            lowest = min(i, lowest)
        return highest_profit