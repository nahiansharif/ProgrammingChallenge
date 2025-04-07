# Problem: Given a string s, find the first non-repeating character and return its index. If it does not exist, return -1.
# Example Input: "leetcode"
# Example Output: 0

def findUniqueCharacter(s):
    char = [letter for letter in s]
    char2 = []
    
    for i in range(len(char)):
        char2 = char[:]
        char2.pop(i)
        if char[i] not in char2:
            return i
    
    return -1

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def findUniqueCharacter2(s):
    char_count = {}  
    
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i

    return -1

# Example usage
s = "leetcode"
index = findUniqueCharacter(s)
print("Index of first non-repeating character:", index)  # Output: 0


s = "leetcode"

print(findUniqueCharacter2(s))