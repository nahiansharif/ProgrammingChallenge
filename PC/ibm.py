def runningSum(arr):
    size = len(arr)
    runSum = size; 
    
    for num in arr:
        runSum += num
    print(runSum)


arr = [10, -5, 4, -2, 3, 1, -1, -6, -1, 0, -5]

runningSum(arr)