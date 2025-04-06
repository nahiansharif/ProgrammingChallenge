# prepare for the interview question
# remember, you failed miserably in paycom interview, but you have 6 months until july to make a great comback. 

lst = []

lst2 = [2, 2, 2, 2, 2, 2]

lst3 = [3] * 5 # this list will have 5 items, each item have value 3 by default. 

lst4 = [4 for i in range(5)] # 5 items with value 4 each

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

index = list.index(4) # it's gonna return index number where value 4 is spotted

if 7 in list:    
    index = list.index(7)
# if val 7 exists, index function will find the location. 

list.insert(4, 100) #insert at item 4 with value 100

for i in range(2, 5):
    list.append(i) #add item at the end of the list

size = len(list)



# Common Methods of List

my_list = [1, 2, 3, 2, 4]

# append(): Add an element to the end of the list
my_list.append(5)
print(f"append(): {my_list}")

# extend(iterable): Add all elements of an iterable (e.g., another list) to the end of the list
my_list = [1, 2, 3, 2, 4, 5]  # Initialize my_list before extend
my_list.extend([6, 7])
print(f"extend(): {my_list}")

# insert(index, val): Insert an item at the defined index
my_list.insert(2, 10)
print(f"insert(): {my_list}")

# pop(index): Removes and returns an element at the given index (default is the last element)
popped_element = my_list.pop(3)
print(f"pop(): {my_list}")
print(f"popped_element: {popped_element}")

# remove(val): Removes the first occurrence of an item from the list
my_list.remove(2)
print(f"remove(): {my_list}")

# clear(): Removes all items from the list
my_list.clear()
print(f"clear(): {my_list}")

my_list = [1, 2, 3, 2, 4] # Resetting the list

# index(val): Returns the index of the first matched item
index_of_2 = my_list.index(2)
print(f"index(): {index_of_2}")

# count(val): Returns the count of the number of items passed as an argument
count_of_2 = my_list.count(2)
print(f"count(): {count_of_2}")

# sort(): Sorts items in a list in ascending order (in place)
my_list.sort()
print(f"sort(): {my_list}")

# reverse(): Reverse the order of items in the list (in place)
my_list.reverse()
print(f"reverse(): {my_list}")

# copy(): Returns a shallow copy of the list
copied_list = my_list.copy()
print(f"copy(): {copied_list}")

#Demonstrating list[::-1]
reversed_list = my_list[::-1]
print(f"list[::-1]: {reversed_list}")

#Demonstrating list[::]
shallow_copy = my_list[::]
print(f"list[::]: {shallow_copy}")
