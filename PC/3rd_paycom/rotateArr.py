# 4. Rotate Array
# Problem: Rotate an array nums of size n to the right by k steps, where k is non-negative.
# Example Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
# Example Output: [5, 6, 7, 1, 2, 3, 4]


def rotateArr(nums, k): 
    
    k = k % len(nums)
    
    return nums[-k:] + nums[:-k]
    
    # nums[-k:] means getting last elements. k = 3, so [-k:] means 012 from the end 
    # nums[:-k] means getting all elements EXCEPT THE LAST ONES. k = 3, so [-k:] means all elements except 012 from the end 
    
    
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

print(rotateArr(nums, k))

