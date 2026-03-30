class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        highest_profit = 0
        
        for price in prices:
            if price < lowest:
                lowest = price
            else:
                highest_profit = max(highest_profit, price - lowest)

        return highest_profit
