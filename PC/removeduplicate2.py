def removeDuplicate2(nums):
    dictNum = {}
    
    for num in nums: 
        dictNum[num] = dictNum.get(num, 0) + 1
    
    nums.clear()
    
    for key, value in dictNum.items():
        
        if value >= 2:
            nums.append(key)
            nums.append(key)
        else:
            nums.append(key)
    
    return len(nums)
    
    
nums = [1,1,1,2,2,3]

print(removeDuplicate2(nums))

nums = [0,0,1,1,1,1,2,3,3]

print(removeDuplicate2(nums))