# https://leetcode.com/problems/edit-distance/description/

# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

class Solution:
    def solve(self, index1, index2, word1, word2):
        if index1 < 0:
            return index2 + 1
        if index2 < 0:
            return index1 + 1
        if word1[index1] == word2[index2]:
            return self.solve(index1 - 1, index2 - 1, word1, word2)
        insertion = 1 + self.solve(index1, index2 - 1, word1, word2)
        deletion = 1 + self.solve(index1 - 1, index2, word1, word2)
        replacement = 1 + self.solve(index1 - 1, index2 - 1, word1, word2)
        return min(insertion, deletion, replacement)

    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        return self.solve(n1 - 1, n2 - 1, word1, word2)
    
class Solution:
    def solve(self, index1, index2, word1, word2, dp):
        if index1 < 0:
            return index2 + 1
        if index2 < 0:
            return index1 + 1
        if dp[index1][index2] != -1:
            return dp[index1][index2]
        if word1[index1] == word2[index2]:
            dp[index1][index2] = self.solve(index1 - 1, index2 - 1, word1, word2, dp)
        else:
            insertion = 1 + self.solve(index1, index2 - 1, word1, word2, dp)
            deletion = 1 + self.solve(index1 - 1, index2, word1, word2, dp)
            replacement = 1 + self.solve(index1 - 1, index2 - 1, word1, word2, dp)
            dp[index1][index2] = min(insertion, deletion, replacement)
        return dp[index1][index2]

    def minDistance(self, word1, word2):
        n1, n2 = len(word1), len(word2)
        dp = [[-1 for _ in range(n2)] for _ in range(n1)]
        return self.solve(n1 - 1, n2 - 1, word1, word2, dp)
    
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        
        for i in range(n1 + 1):
            dp[i][0] = i
        for j in range(n2 + 1):
            dp[0][j] = j
        
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    insertion = 1 + dp[i][j - 1]
                    deletion = 1 + dp[i - 1][j]
                    replacement = 1 + dp[i - 1][j - 1]
                    dp[i][j] = min(insertion, deletion, replacement)
        
        return dp[n1][n2]
    
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        prev = [j for j in range(n2 + 1)]
        curr = [0] * (n2 + 1)
        
        for i in range(1, n1 + 1):
            curr[0] = i
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    insertion = 1 + curr[j - 1]
                    deletion = 1 + prev[j]
                    replacement = 1 + prev[j - 1]
                    curr[j] = min(insertion, deletion, replacement)
            prev = curr[:]
        
        return prev[n2]
    
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        prev = list(range(len(word2)+1))
        cur = [0] * (len(word2) + 1)

        for i in range(1, len(word1)+1):
            cur[0] = i
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    cur[j] = prev[j-1]
                else:
                    cur[j] = min(prev[j-1] + 1, prev[j] + 1, cur[j-1] + 1)
                
            prev = cur
            cur = [0] * (len(word2) + 1)
        
        return prev[-1]
    
class Solution:
  def minDistance(self, word1: str, word2: str) -> int:
    m = len(word1)
    n = len(word2)
    # dp[i][j] := min # Of operations to convert word1[0..i) to word2[0..j)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
      dp[i][0] = i

    for j in range(1, n + 1):
      dp[0][j] = j

    for i in range(1, m + 1):
      for j in range(1, n + 1):
        if word1[i - 1] == word2[j - 1]:
          dp[i][j] = dp[i - 1][j - 1]
        else:
          dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    return dp[m][n]

