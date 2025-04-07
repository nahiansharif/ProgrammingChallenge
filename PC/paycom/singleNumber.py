def singleNumber(nums):
        count_map = {}
        
        # Count occurrences of each number
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
        
        # Find the number that appears only once
        for num, count in count_map.items():
            if count == 1:
                return num
    # if(len(nums) == 1):
    #     return nums[0]
    
    # num2 = []
    # for i in range(0, len(nums)):
    #     for j in range(0, len(nums)):
    #         if(j == i):
    #             continue
    #         elif(nums[i] == nums[j]):            
    #             num2.append(nums[i])
    #             break
                
    
    # for i in range(0, len(nums)):
    #     try:
    #         if nums[i] != num2[i]:
    #             return nums[i]
    #     except:
    #         return nums[i]
                
                
num = [2,2,1]

print(singleNumber(num))

num = [4,1,2,1,2]

print(singleNumber(num))

num = [1]

print(singleNumber(num))

num = [1,3,1,-1,3]

print(singleNumber(num))

