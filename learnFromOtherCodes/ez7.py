# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight). 

# https://leetcode.com/problems/number-of-1-bits/description/ 

class Solution(object):
    def hammingWeight(self, n):
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
    
    
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0  # ✨ Soul counter
        while n:
            n = n & (n - 1)  # ⚔️ Slash away the lowest spiritual spark
            res += 1  # 🔥 Count each vanquished spark
        return res  # 💫 Return the number of souls still glowing
    
import collections    
def using_inbuilt_counter(self, n):
        counter = collections.Counter(bin(n)[2:])
        return counter.get("1", 0)
    
def using_bit_manipulation(self, n):
        count = 0
        while n:
            if n & 1: count += 1
            n = n >> 1
        return count