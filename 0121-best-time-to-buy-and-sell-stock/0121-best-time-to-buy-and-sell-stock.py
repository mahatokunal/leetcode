class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minm = prices[0]
        maxm_profit = 0
        for i in range(1, n):
            maxm_profit = max(prices[i]-minm, maxm_profit)
            minm = min(prices[i], minm)
        return maxm_profit