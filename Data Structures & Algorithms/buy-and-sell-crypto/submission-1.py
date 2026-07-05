class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_buy = prices[0]
        for sell in prices:
            profit = max(profit, sell - min_buy)
            min_buy = min(min_buy, sell)
        return profit