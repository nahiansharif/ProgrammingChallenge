def diagonalDifference(arr):
    d = 0
    d2 = 0
    
    for i in range(0, len(arr)):
        d += arr[i][i]
        d2 += arr[i][-i - 1]

    return abs(d - d2)
      

    


arr = [[1, 2, 3], 
       [4, 5, 6],
       [9, 8, 9]]

print(diagonalDifference(arr))