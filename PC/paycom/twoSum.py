def twoSum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if(nums[i] + nums[j] == target):            
                return i, j
            
            
            
nums = [2,5,5,11]
target = 10

r = twoSum(nums, target)

print(r)