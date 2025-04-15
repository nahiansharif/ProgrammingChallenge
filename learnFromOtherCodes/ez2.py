# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        seen = {}

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
