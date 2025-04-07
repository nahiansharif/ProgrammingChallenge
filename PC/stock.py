class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit

# Example usage
prices = [7, 1, 5, 3, 6, 4]
solution = Solution()
print(solution.maxProfit(prices))  # Output: 5


prices = [2, 4, 1]
solution = Solution()
print(solution.maxProfit(prices))  # Output: 5
