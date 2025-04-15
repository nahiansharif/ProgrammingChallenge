# prepare for the interview question
# remember, you failed miserably in paycom interview, but you have 6 months until july to make a great comback. 

# this splits the word when there's a space. 
s = "hello, world!"
word = s.split(" ")
print(f"# 1: split: {word}")

# this split word based on space by default. 
s = "I am from Planet Namik"
word = s.split()
print(f"# 2: split based on space by default: {word}")

# this will split string when there's a. 
word = s.split("a")
print(f"# 3: split based on a: {word}")

# upper and lowercase 
upper = s.upper()
lowercase = upper.lower()
print(f"# 4: upper and lowercase: {upper, lowercase}")

# this function returns only characters and numbers. anything else is being replaced with nothing
import re 
s = "!I am fr@om%/ Pla3n&et# N*am#$+ik"
cleantext = re.sub(r'[^a-zA-Z0-9\s]', '', s)
print(f"# 5: clean text: {cleantext, len(s), len(cleantext)}")

# size & last letter
size = len(s)
lastChar = s[-1]
print(f"# 6: size and last character: {size, lastChar}")

sliced = s[0:5]
name = "lalu"
greetings = sliced + ", " + name
print(f"# 7: concatenated: {sliced, greetings}")
# concatenated 

# add space to every character and join. 
balloon = "Sammy has a balloon"
joinStr = " ".join(balloon)
print(f"# 8: join the space between lettters: {balloon, joinStr}")


s = "Nahian Sharif"

#convert each character into array of lists. 
char = list(s)
#join all characters into one string
joinedStr =  "". join(char ) 
print(f"# 9: array strings : {balloon, joinStr}")

# replace functionalities
s = "Ali is the king"
s = s.replace("Ali", "Kobalis")
s = s.replace("the ", "")
print(f"# 10: replace : {s}")

char2int = ord("N")
int2Char = chr(65)
# convert letter to number & number to letter. 
print(f"# 11: char number and number to char : {char2int, joinStr}")


# page 
# Counts the occurrences of a substring with optional start and end position

text = "the quick the brown fox jump over the lazy white dog"
countThe = text.count("the")
print(f"# 12: count the number of occurance of the : {countThe}")

# Returns the index of the first occurrence of a substring or returns -1 if the substring is not found

email = "naina@gmail.com"
atIndex = email.find("@")
username = email[:atIndex]
print(f"# 13: email and username : {email, username}")


# Converts the string to all lowercase or uppercase 

txt = "        Hello        World       "

print(f"# 14: removing spaces on left & right side of word : {txt, txt.strip()}")
print(f"# 15: removing spaces left side of word : {txt, txt.lstrip()}")
print(f"# 16: removing spaces right side of word : {txt, txt.rstrip()}")

txt = "hello world it will be a lovely day lily"
s = txt.replace("l","zyz")
print(f"# 17: replaces : {txt, s}")

name = "Mr. Nahian Sharif"
if name.startswith("Mr."):
    print("# 18: its a boy")
else: 
    print("# 18: its a girl")

word = "fighting"
if word.endswith("ing"):
    print("# 19: verb word")
else: 
    print("# 19: no idea what this word is ")

# find function looks for first occurance of the letter and returns the position of the first occurance
s = txt.find("l")
print(f"# 20: finding l : {txt, s}")


#converting 
num = 42
str_num = str(num)

str_num = "42"
num = int(str_num)

#frequency counter: see how many times each letter appeared in a string
# it's sorted from big value to small value 

from collections import Counter
print(f"# 21: frequency ccounter of str: {txt, Counter(txt)}")

# palindrome check
def palindrome(s):
    return s == s[::-1]

# anagram check 
def anagrams(s1, s2):
    return sorted(s1) == sorted(s2)
 # character count using dictionary

from collections import defaultdict
count = defaultdict(int)

for ch in txt:
    count[ch] = count[ch] + 1

print(f"# 22: frequency ccounter of str using default dict: {txt, count}")

# find first unique character: 

def findUnique(txt):
    count = Counter(txt)
    # we get the position and value of each letter in the string
    # we use each letters as keys and see if the value of the key in count is 1 or not. 
    for i, ch in enumerate(txt):
        if count[ch] == 1:
            return i
    return -1
print("\n")
print(sorted(txt), txt, tuple(sorted(txt)))

def groupAnagram(strs):
    from collections import defaultdict
    res = defaultdict(list)
    for s in strs:
        # tuple makes a list
        key = tuple(sorted(s))
        res[key].append(s)
    return list(res.values())

def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

