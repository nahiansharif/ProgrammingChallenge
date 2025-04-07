def missingNumber(nums):
    nums.sort()
    for i in range(len(nums)):
        if i != nums[i]:
            return i
    return len(nums)  
      
        
nums = [3,0,1]

print(missingNumber(nums))

nums = [0,1]

print(missingNumber(nums))

nums = [9,6,4,2,3,5,7,0,1]

print(missingNumber(nums))