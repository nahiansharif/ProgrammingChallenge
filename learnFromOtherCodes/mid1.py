# https://leetcode.com/problems/perfect-squares/description/ 

# Given an integer n, return the least number of perfect square numbers that sum to n.

# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

class Solution(object):
    def numSquares(self, n):
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1

        return dp[n]
    
    
class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)
    
    def helper(self, n: int, memo: dict) -> int:
        if n == 0:
            return 0
        if n < 0:
            return 0
        if n in memo:
            return memo[n]
        
        min_count = float('inf')
        i = 1
        while i * i <= n:
            curr = 1 + self.helper(n - i * i, memo)
            min_count = min(min_count, curr)
            i += 1
        
        memo[n] = min_count
        return min_count
    
    
