# Problem: Given an array containing n distinct numbers taken from the range 0 to n, find the one missing number.
# Example Input: [3, 0, 1]
# Example Output: 2
# Follow-Up: Solve it with O(n) time complexity and O(1) space.

def findMissingNum(nums):
    
    for i in range(0, len(nums)):
        if i not in nums:
            print(i)
            break
        
nums = [3, 0, 1]

findMissingNum(nums)
