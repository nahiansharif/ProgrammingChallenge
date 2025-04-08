# prepare for the interview question
# remember, you failed miserably in paycom interview, but you have 6 months until july to make a great comback. 


# append extend insert pop remove clear copy index count sort sorted reverse set jump half flat shuffle filter map reduce swap absolute hashmap rotation prime ::-1  :: 
lst = []

lst2 = [2, 2, 2, 2, 2, 2]

lst3 = [3] * 5 # this list will have 5 items, each item have value 3 by default. 

lst4 = [4 for i in range(5)] # 5 items with value 4 each

list9 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

index = list9.index(4) # it's gonna return index number where value 4 is spotted

if 7 in list9:    
    index = list9.index(7)
# if val 7 exists, index function will find the location. 

list9.insert(4, 100) #insert at index 4 with value 100

for i in range(2, 5):
    list9.append(i) #add item at the end of the list
    
size = len(list9)

num = 0

# Common Methods of List

my_list = [1, 2, 3, 2, 4]
originalList = my_list.copy()

 

# append(): Add an element to the end of the list
my_list.append(7)
print(f"\n # 1 original: {originalList} append(): {my_list}")
originalList = my_list.copy()

 
# extend(list): Add a list at the end of the main list 

my_list.extend([6, 12, 15]) 
print(f"\n # 2 original: {originalList} extend(): {my_list}")


 
# insert(index, val): Insert an item at the defined index
my_list.insert(2, 10)
print(f"\n # 3 original: {originalList} insert(): {my_list}")
originalList = my_list.copy()

 
# pop(index): 
# Removes the item from the specified index or position
# You can also store the removed item's value, but it won't be in the array 
popped_element = my_list.pop(2)
print(f"\n # 4 original: {originalList} popped_element: {popped_element} List: {my_list}")
originalList = my_list.copy()

# remove last index from the list
my_list.pop()
print(f"\n # 4.5 original: {originalList} pop(): {my_list}")
originalList = my_list.copy()

 
# remove(val): Removes the first occurrence of an item from the list
my_list.remove(2)
print(f"\n # 5 original: {originalList} remove(): {my_list}")
originalList = my_list.copy()

 
# clear(): Removes all items from the list
my_list.clear()
print(f"\n # 6 original: {originalList} clear(): {my_list}")
originalList = my_list.copy()

my_list = [1, 2, 3, 2, 4, 2] # Resetting the list
originalList = my_list.copy()

 
# index(val): Returns the index of the first matched item
index_of_2 = my_list.index(3) # value 3 exists in position 2
print(f"\n # 7 original: {originalList} index(): {index_of_2}")
originalList = my_list.copy()

 
# count(val): This counts the number of time this item appeared in the list. 
count_of_2 = my_list.count(2)
print(f"\n # 8 original: {originalList} count(): {count_of_2}")
originalList = my_list.copy()

 
# sort(): Sorts items in a list in ascending order (from small to big numbers)
my_list.sort()
print(f"\n # 9 original: {originalList} sort(): {my_list}")
originalList = my_list.copy()

# Creates a new sorted list
sorted_num = sorted(my_list)  
print(f"\n # 9.5 original: {my_list} sorted: {sorted_num}")

 
# reverse(): Reverse the order of items in the list (in place)
my_list.reverse()
print(f"\n # 10 original: {originalList} reverse(): {my_list}")
originalList = my_list.copy()

 
# copy(): Returns a shallow copy of the list
copied_list = my_list.copy()
print(f"\n # 11 original: {originalList} copy(): {copied_list}")


 
# another way to reverse 
reversed_list = my_list[::-1]
print(f"\n # 12 original: {originalList} list[::-1]: {reversed_list}")


 
#another way to copy list 
shallow_copy = my_list[::]
print(f"\n # 13 original: {originalList} list[::]: {shallow_copy}")


 
# duplicated removed
print(f"\n # 14 original: {my_list} duplicated removed: {set(my_list)}")


# skip elements in a list by a specific step size n
# you can jump from elements to elements by a number of times. 

my_list= [1, 2, 3, 4, 5, 6, 7, 8, 9]
 
print(f"\n # 15 original: {my_list} skip elements by 2, 3, and 4 times: \n")
print(my_list[::2])
print(my_list[::3])
print(my_list[::4]) 

# get first half of the array 
first_half = my_list[:len(my_list)//2]
 
print(f"\n # 16 original: {my_list} first half: {first_half}")

# get last half of the array 
last_half = my_list[len(my_list)//2:]
 
print(f"\n # 17 original: {my_list} last half: {last_half}")

# get last index 
 
print(f"\n # 18 original: {my_list} last element: {my_list[-1]}")

# conditional list comprehension 
# Find even numbers
even_numbers = [num for num in my_list if num % 2 == 0]

# Find odd numbers
odd_numbers = [num for num in my_list if num % 2 != 0]

print(f"\n # 19 original: {my_list} even nums: {even_numbers} odd nums: {odd_numbers}")

# combining nested list (list of lists) into a single list
nested = [[1, 2, 3], [4, 5], [6]]
flat = [item for sublist in nested for item in sublist]
print(f"\n # 20 original: {nested} after flattening: {flat}")

# Shuffles a list
originalList = my_list.copy()
import random as rnd

#overrides the list and shuffles it 
rnd.shuffle(my_list) 

#pick 3 random index from the list
sample = rnd.sample(my_list, 3)
print(f"\n # 21 original: {originalList} Override shuffles the whole list: {my_list} pick random number of item from the list: {sample}")
my_list = originalList.copy()

# use filter to get specific number of items from the list based on condition. 
evens = list(filter(lambda x: x % 2 == 0, my_list))
print(f"\n # 22 original: {my_list} filtered Evens: {evens}")

# use map to perform tasks with all elements
squared = list(map(lambda x: x % 3, my_list))
print(f"\n # 23 original: {my_list} map sqaured: {squared}")

# perform tasks with all the elements and reduce them into 1 item 
# have default value in the last argument to avoid errors that occur in empty lists. 
import functools
add= functools.reduce(lambda x, y: x + y, my_list, 0)
subtract= functools.reduce(lambda x, y: x - y, my_list, 0) 
mul= functools.reduce(lambda x, y: x * y, my_list, 1) 
divide= functools.reduce(lambda x, y: x / y, my_list, 1) 
print(f"\n # 24 original: {my_list} add: {add}  subtract: {subtract} mul: {mul} divide: {divide}")

# swap elements
originalList = my_list.copy()
my_list[1], my_list[3], my_list[5] = my_list[5], my_list[1], my_list[3]
print(f"\n # 25 original: {originalList} swaped: {my_list}")
my_list = originalList.copy()


# Sort by absolute value
my_list = [-3, -1, 2, -2]
s = my_list.copy()
my_list.sort(key=abs)  
print(f"\n # 26 original: {s} absolute sorted: {my_list}")
my_list = originalList.copy()

# create a hasmap with array as values.  
indexed_dict = {i: val for i, val in enumerate(my_list)}
print(f"\n # 27 original: {my_list} dict: {indexed_dict}")

a = [1, 2, 3]
b = [1, 2, 3]
print(f"\n # 28 compare: {a == b}")

# arr[-n:] means you get the last n elements from the list
# arr[:-n] means you get every element except the last n elements.
# arr[n:] means you get every element except the first n elements.
# arr[:n] means you get the first n elements from the list, starting from the beginning
# [-2:] neg + left = get last 2 index
# [:-2] neg + right = get everything except last 2
# [2:] pos + left = get everything except first 2 
# [:2] pos + right - get first 2 

print(f"\n # 29 original: {my_list}")
print(my_list[-2:]) #nl = last
print(my_list[:-2]) #nr = eel
print(my_list[5:]) #pl = eef
print(my_list[:5]) #pr = first


rotated = my_list[-2:] + my_list[:-2]
print(f"\n # 30 original: {my_list} ROTATED: {rotated}")


# geneate a list of prime numbers from 0 to n 

import itertools as it
import math as ma

#thsi function checks if the n is a prime number or not. 
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    return not any(n%i == 0 for i in it.islice(it.count(2), ma.floor(ma.sqrt(n)-1)))
# ANY means if any of the condition is true, it will be accepted. but NOT makes it the opposite. So if any of the condition is true, it will be false. 
# n%i == 0 checks if n is divisible by I 
# for i in.... this is part of the number generator that produces the sequence of divisors to test against n
# it.count(2) means the starting point in this generator is 2 to infinite 
# itertools.islice cuts the sequence from infinite to ma.floor(ma.sqrt(n) - 1) 
# ma.sqrt(n) square root of n 
# - 1 ensures you only check up to the largest integer less than the square root of n.
# ma.floor() rounds down to the nearest integer.


def the_primes(n):
    return list(filter(lambda x: is_prime(x), it.takewhile(lambda x: x < n, it.count(2))))


primeNums = the_primes(101)
print(f"\n # 31 prime numbers {primeNums}")
print(f"\n # 32 is 10 prime numbers? {is_prime(10)}")
print(f"\n # 33 is 31 prime numbers? {is_prime(31)}")

import math
gcd_result = functools.reduce(math.gcd, my_list)
print(f"\n # 34 original: {my_list} GCD: {gcd_result}")



print("\n")