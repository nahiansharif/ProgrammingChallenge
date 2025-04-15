# prepare for the interview question
# remember, you failed miserably in paycom interview, but you have 6 months until july to make a great comback. 

# create hashmap with no value

myVar = {}

# create hashmap with default value

my_map = {"alice": 88, "bob": 77, "popi": 82}

# get value of a specific key
print(f"# 1: default value: {my_map["alice"]}")  # Output: 88

# add and update new entries:
my_map["charlie"] = 99  # Add new entry
my_map["alice"] = 90    # Update existing entry

print(f"# 2: value: {my_map}")  

# Check if key exists 
if "bob" in my_map:
    print("# 3: Bob is in the map!")  # Output: Bob is in the map!

# remove a key and its value:
my_map.pop("alice")  # Removes 'alice' from map
del my_map["popi"] # this is another way
print(f"# 4: after removing value: {my_map}")         # {'bob': 77, 'charlie': 99}

# length of hashmap:

print(f"# 5: length of hasmap: {len(my_map)}")   

# iterate using keys only: 

for key in my_map:
    print(f"# 6: iterate hasmap with keys only: {key, my_map[key]}" )

# iterate and get both keys and its value: 

for key, value in my_map.items():
    print(f"# 7: iterate hasmap with keys and its value: {key}: {value}")


# print all keys in hashmap: 
print(f"# 8: print all keys in hashmap: {my_map.keys()}" )

# print all values in hashmap: 
print(f"# 9: print all values in hashmap: {my_map.values()}" )

# print all keys & values in hashmap: 
print(f"# 10: print all keys & values in hashmap: {my_map.items()}" )

# if the key "daniel" exists, this function is gonna return the value of the key. 
# if the key "daniel" dont exists, it's going to return the value, but it won't create a new key.

value = my_map.get("daniel", 0)
print(f"# 11: print all values in hashmap: {value}")  # Output: 0 (default)

# Dictionary Length
len(my_map)

# create integer hashmap with default values for each key. 
from collections import defaultdict

freq = defaultdict(int)
freq["apple"] += 1

# Counts items in a list or string as dictionary.
from collections import Counter

words = ["a", "b", "a", "c"]
count = Counter(words)
print(f"# 12: print amount of times 'a' appeared in hashmap: {count["a"]}" )  # 2

# dictionary comprehension: 
squares = {x: x * x for x in range(5)}

# nested dictionary 

users = {
    "alice": {"age": 25, "city": "NY"},
    "bob": {"age": 30, "city": "LA"}
}
print(f"# 13: print nested hashmap: {users["alice"]["city"]}" )

# Use setdefault() to initialize values if not present:
my_map.setdefault("apple", 0) 

######################################################################################################################################

# Find the max number of times an item appeared in the list. 

def item_appeared_counter(arr):
    count = {}
    for x in arr:
        count[x] = count.get(x, 0) + 1
    
    maxNumKey = max(count, key=count.get)
    return maxNumKey

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

# Group Anagrams

from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        groups[key].append(word)
    return list(groups.values())
