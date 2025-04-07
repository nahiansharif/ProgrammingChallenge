#
# 

def jump(arr):
    # first index = 0
    # last index = len(arr) - 1
    for i in range(1, len(arr)):
        i = i + arr[i]
        if i == (len(arr) - 1):
            return True


    return False

arr = [2, 3, 1, 1, 4]
print(jump(arr))

arr = [3, 2, 1, 0, 4]
print(jump(arr))

arr = [3, 2, 1, 6, 4, 1, 2, 1, 5, 9, 7, 8, 2]
print(jump(arr))

arr = [3, 2, 1, 6, 4, 1, 2, 1, 5, 3, 7, 8, 2]
print(jump(arr))