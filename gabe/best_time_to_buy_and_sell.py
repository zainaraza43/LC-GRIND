class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
       
        max_profit = 0
        
        low = 0
        i = 1

        
        for i in range(1, len(prices)):
            current_profit = prices[i] - prices[low]
            
            if prices[low] < prices[i]:
                max_profit = max(current_profit, max_profit)
            else:
                low = i
            
                
        return max_profit