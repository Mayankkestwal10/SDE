# Buy and Sell Stock - I (LeetCode)

import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if(len(prices)==0 or len(prices)==1):
            return 0
        
        profit = -math.inf
        
        min_price = prices[0]
        
        for i in range(1, len(prices)):
            pot = prices[i]-min_price
            min_price = min(prices[i], min_price)
            profit = max(pot, profit)
            
        if(profit<=0):
            return 0
        return profit



# Buy and Sell Stock - II 

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        
        sell = 0
        
        for i in range(1, n):
            if(prices[i]>prices[i-1]):
                sell = sell + prices[i] - prices[i-1]
            else:
                pass
        
        return sell