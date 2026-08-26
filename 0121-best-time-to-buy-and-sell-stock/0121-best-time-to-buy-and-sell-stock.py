class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mini_buy = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            if prices[i]<mini_buy:
                mini_buy = prices[i]
            profit = prices[i]-mini_buy

            if profit > max_profit:
                max_profit = profit 
        return max_profit

        