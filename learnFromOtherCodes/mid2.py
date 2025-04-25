# https://leetcode.com/problems/bulls-and-cows/ 

# You are playing the Bulls and Cows game with your friend.

# You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

# The number of "bulls", which are digits in the guess that are in the correct position.
# The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
# Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

# The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

class Solution(object):
    def getHint(self, secret, guess):
        bull, cow = 0, 0
        s = {} # secret hashtable
        g = {} # guess hashtable
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                s[secret[i]] = s.get(secret[i], 0) + 1
                g[guess[i]] = g.get(guess[i], 0) + 1
        
        for k in s:
            if k in g:
                cow += min(s[k], g[k])
        
        return '{0}A{1}B'.format(bull, cow)
    
    
import collections
import operator

def getHint(self, secret, guess):
    bulls = sum(map(operator.eq, secret, guess))
    both = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
    return '%dA%dB' % (bulls, both - bulls)

def getHint(self, secret, guess):
        A = sum(a==b for a,b in zip(secret, guess))
        B = collections.Counter(secret) & collections.Counter(guess)
        return "%dA%dB" % (A, sum(B.values()) - A)
    
    
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull=0
        for i in range(len(secret)):
            bull += int(secret[i] == guess[i])
        
        cows=0
        for c in set(secret):
            cows += min(secret.count(c), guess.count(c))
        
        return f"{bull}A{cows-bull}B"
    
from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # Dictionary for Lookup
        lookup = Counter(secret)
        
        x, y = 0, 0
        
        # First finding numbers which are at correct position and updating x
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                x+=1
                lookup[secret[i]]-=1
        
        # Finding numbers which are present in secret but not at correct position 
        for i in range(len(guess)):
            if guess[i] in lookup and secret[i] != guess[i] and lookup[guess[i]]>0:
                y+=1
                lookup[guess[i]]-=1
        
		# The reason for using two for loop is in this problem we have 
		# to give first priority to number which are at correct position,
		# Therefore we are first updating x value
		
        return "{}A{}B".format(x, y)