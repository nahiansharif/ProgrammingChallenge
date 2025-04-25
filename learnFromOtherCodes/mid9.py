# https://leetcode.com/problems/factorial-trailing-zeroes/ 


# Given an integer n, return the number of trailing zeroes in n!.

# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1. 

class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n > 0:
            n //= 5
            res += n
        return res
    

class Solution(object):
    def trailingZeroes(self, n):
        count = 0
        divisor = 5

        while n >= divisor:
            count += n // divisor
            divisor *= 5

        return count
    
    
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''sum=1
        cnt=0
        while n:
            sum=sum*n
            if(sum>=10):
                if(sum%10==0):
                    cnt=cnt+1
                sum=sum/10
            n=n-1
        if(cnt==0):
            return 0
        return cnt'''
        cnt=0
        while n:
            n/=5
            cnt+=n
        return cnt

class Solution:
    def trailingZeroes(self, n: int) -> int:
        fives = 0
        i = 5
        while i <= n:
            fives += n // i
            i *= 5
        return fives
    
class Solution(object):
    def trailingZeroes(self, n):
        
        return n//5 + n//25 + n//125 + n//625 + n//3125
        