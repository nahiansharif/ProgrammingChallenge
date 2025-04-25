# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

def containsNearbyDuplicate(nums, k):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] == nums[j]:
                    if abs(i - j) <= k:
                        return True
        return False

def containsNearbyDuplicate(nums, k):
        x = {}
        for i in range(len(nums)):            
            # Check if the difference in indices matches k
            # x[nums[i]] is the value from hashmap
            # nums[i] is the key for hashmap 
            # (nums[i] in x) is the same as nums[i] == nums[j]
            # abs(i - x[nums[i]]) <= k is the same as abs(i - j) <= k
            
            if (nums[i] in x) and (abs(i - x[nums[i]]) <= k):
                return True
            x[nums[i]] = i 
                
        return False
        



class Solution:
    def containsNearbyDuplicate(self, nums, k):
        seen = {}
        
        # this for loop iterates the whole array
        # val has the value of the array 
        # i holds the current position 
        
        
        for i, val in enumerate(nums):
            if val in seen and i - seen[val] <= k:
                return True
            else:
                seen[val] = i
        
        return False
    
    
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        seen = set()

        for i, val in enumerate(nums):
            if i > k:
                seen.remove(nums[i - k - 1])

            if val in seen:
                return True

            seen.add(val)

        return False
    
from collections import deque

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        window = deque()
        seen = set()

        for i, val in enumerate(nums):
            if val in seen:
                return True
            
            window.append(val)
            seen.add(val)

            if len(window) > k:
                removed = window.popleft()
                seen.remove(removed)

        return False
