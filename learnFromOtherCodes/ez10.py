# https://leetcode.com/problems/move-zeroes/ 

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements. 

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nonzero, i = 0, 0  # Initialize pointers
        n = len(nums)
        while i < n:
            if nums[i] != 0:
                # Swap non-zero element with the element at the `nonzero` pointer
                nums[i], nums[nonzero] = nums[nonzero], nums[i]
                nonzero += 1  # Move `nonzero` pointer
            i += 1  # Move `i` pointer 
            
class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
                
class Solution(object):
    def moveZeroes(self, nums):

        non_zero = 0  # Pointer for non-zero elements
        
        # Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[non_zero] = nums[non_zero], nums[i]
                non_zero += 1


    def moveZeroes(self, nums):
        n = len(nums)
        i = 0
        for j in range(n):
            if (nums[j] != 0):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                
                
# in-place
def moveZeroes(self, nums):
    zero = 0  # records the position of "0"
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1
            
class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        end = len(nums)
        while i < end:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                end -= 1
            else:
                i += 1
                
class Solution:
    def moveZeroes(self, nums: list) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1