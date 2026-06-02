class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0 
        l = len(prices)

        max_diff = 0
        for i in range(l-1):

            diff = 0

            j = i+1
            while j <= (l-1):
                
                diff = max(prices[j] - prices[i], diff)
                j += 1
            
            max_diff = max(max_diff, diff)

        return max_diff
