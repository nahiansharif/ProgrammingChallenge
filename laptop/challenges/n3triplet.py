# Given an array arr, find all unique triplets (i, j, k) such that arr[i] + arr[j] + arr[k] == 0 and i != j != k

arr = [-1, 0, 1, 2, -1, -4] # [[-1, -1, 2], [-1, 0, 1]]

nums = []


# i + 1, j + 1 don't go out of bound. For loops stops 
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            print(i, j, k)
            if arr[i] + arr[j] + arr[k] == 0:
                nums.append([arr[i], arr[j], arr[k]])
        
                
                
                
print(nums)
# so, for loops continue to run without error, but if you try to access index of an array with out of bound for loop iteration


# ---------------------------------------------------------------------------------------------------------------------------------------
x = {}
y = {}

for i in range(len(arr)):
    
    
                