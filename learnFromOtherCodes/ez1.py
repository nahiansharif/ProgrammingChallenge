# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        ans=0
        pointer=len(columnTitle)-1

        for i in range(len(columnTitle)):
            pos = ord(columnTitle[i])-ord('A')+1
            ans += int(pos*(26**pointer))
            pointer -= 1

        return ans    
        
        
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0

        for char in columnTitle:
            ans = ans * 26 + (ord(char) - ord('A') + 1)

        return ans


def str2num_recursively(s):
    def _helper(s, res):
        if not s: return res
        return _helper(s[1:], res * 10 + int(s[0]))
    return _helper(s, 0)


def titleToNumber(s):
    res = 0
    val = [i for i in range(1, 27)]
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    d = dict(zip(letters, val))
    for ch in s:
        res = res * 26 + d[ch]
    return res