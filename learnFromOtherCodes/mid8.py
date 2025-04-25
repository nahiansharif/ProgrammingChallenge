# https://leetcode.com/problems/word-break/description/

# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set= set(wordDict)
        dp= [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            dp[i] = any(dp[j] and s[j:i] in word_set for j in range(i))

        return dp[len(s)]
    
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        word_set = set(wordDict)
        memo = {}

        def backtrack(index):
            if index == len(s):
                return True
            if index in memo:
                return memo[index]

            for word in word_set:
                if s.startswith(word, index):
                    if backtrack(index + len(word)):
                        memo[index] = True
                        return True

            memo[index] = False
            return False
        return backtrack(0)
    
    
def wordBreak(self, s, words):
    ok = [True]
    for i in range(1, len(s)+1):
        ok += any(ok[j] and s[j:i] in words for j in range(i)),
    return ok[-1]

def wordBreak(self, s, words):
    ok = [True]
    max_len = max(map(len,words+['']))
    words = set(words)
    for i in range(1, len(s)+1):
        ok += any(ok[j] and s[j:i] in words for j in range(max(0, i-max_len),i)),
    return ok[-1]

class Solution:
    def __init__(self):
        self.dp = {}

    def solve(self, s, m):
        if not s:
            return True
        if s in self.dp:
            return self.dp[s]
        for i in range(len(s)):
            r = s[:i + 1]
            if r in m:
                if self.solve(s[i + 1:], m):
                    self.dp[s] = True
                    return True
        self.dp[s] = False
        return False

    def wordBreak(self, s, wordDict):
        m = set(wordDict)
        return self.solve(s, m)
    
class TrieNode:
    def __init__(self, character):
        self.character = character
        self.children = [None] * 26
        self.is_end_of_word = False

class Solution(object):
    def __init__(self):
        self.root = TrieNode('\0')

    def insert_word(self, root, word):
        current_node = root
        for c in word:
            index = ord(c) - ord('a')
            if current_node.children[index] is None:
                current_node.children[index] = TrieNode(c)
            current_node = current_node.children[index]
        current_node.is_end_of_word = True

    def can_segment_string(self, root, s, start, memo):
        if start == len(s):
            return True

        if memo[start] != -1:
            return memo[start] == 1

        current_node = root
        for i in range(start, len(s)):
            index = ord(s[i]) - ord('a')
            if current_node.children[index] is None:
                memo[start] = 0
                return False
            current_node = current_node.children[index]
            if current_node.is_end_of_word and self.can_segment_string(root, s, i + 1, memo):
                memo[start] = 1
                return True
        memo[start] = 0
        return False

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        for word in wordDict:
            self.insert_word(self.root, word)
        memo = [-1] * len(s)
        return self.can_segment_string(self.root, s, 0, memo)