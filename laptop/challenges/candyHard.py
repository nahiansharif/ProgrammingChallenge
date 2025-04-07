#
# 

def candy(arr):

    darr = [1] * len(arr)

    # Left to right
    for i in range(1, len(arr)):
        if(arr[i] > arr[i-1]):
            darr[i] += 1

    # right to left
    for i in range(len(arr)-2, -1, -1):
        if(arr[i] > arr[i+1]):
            darr[i] += 1 

    print(darr)


    return sum(darr)

arr = [1, 0, 2]
print(candy(arr))

arr = [1, 2, 2]
print(candy(arr))

arr = [1, 2, 3, 2, 1]
print(candy(arr))

arr = [5, 4, 3, 5, 6, 2]
print(candy(arr))