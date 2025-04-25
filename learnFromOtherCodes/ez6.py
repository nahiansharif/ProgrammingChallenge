# https://leetcode.com/problems/excel-sheet-column-title/description/

#  Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

class Solution(object):
    def convertToTitle(self, columnNumber):
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            result.append(chr(columnNumber % 26 + 65))
            columnNumber //= 26
        return "".join(result[::-1])
    
class Solution(object):
    def convertToTitle(self, columnNumber):
        output = ""
        while columnNumber > 0:
            output = chr(ord('A') + (columnNumber - 1) % 26) + output
            columnNumber = (columnNumber - 1) // 26
        return output
    
    
class Solution:
    def convertToTitle(self, num):
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while num > 0:
            result.append(capitals[(num-1)%26])
            num = (num-1) // 26
        result.reverse()
        return ''.join(result)
    
    
class Solution(object):
    def convertToTitle(self, columnNumber):
        result=""
        while columnNumber>0:
            columnNumber -= 1
            latter=chr((columnNumber%26)+65)
            result=latter+result
            columnNumber//=26
        return result
    
    
def convertToTitle(num: int) -> str:
        s = ""
        
        while num > 0:
            num,rem = divmod(num-1,26)
            s += chr(65+rem)
        
        return s[::-1]
    
    
def convertToTitle(self, n):
    r = ''
    while(n>0):
        n -= 1
        r = chr(n%26+65) + r
        n /= 26
    return r