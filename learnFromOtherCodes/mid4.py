# https://leetcode.com/problems/product-of-array-except-self/ 

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n
        for i in range(n):
            for j in range(n):
                if i != j:
                    ans[i] *= nums[j]
        return ans
    
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        ans = [1] * n
        
        # Fill prefix array
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        # Fill suffix array
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        # Calculate the result
        for i in range(n):
            ans[i] = prefix[i] * suffix[i]
        
        return ans
    
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        ans = [1] * n

        # Calculate prefix products
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]

        prevSuffix = 1
        # Calculate suffix products and update ans array
        for i in range(n - 2, -1, -1):
            prevSuffix *= nums[i + 1]
            ans[i] *= prevSuffix

        return ans
    
# Here I have used division operation

class Solution(object):
    def productExceptSelf(self, nums):
        total_product = 1
        zero_count = 0
        
        for num in nums:
            if num != 0:
                total_product *= num
            else:
                zero_count += 1
                
        result = []
        
        if zero_count > 1:
            return [0] * len(nums)
        
        for num in nums:
            if num != 0:
                if zero_count == 1:
                    result.append(0)
                else:
                    result.append(total_product // num)
            else:
                result.append(total_product)
        
        return result
    
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n

        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer
    
