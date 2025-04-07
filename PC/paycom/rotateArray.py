def rotate(self, nums, k):
        k = k % len(nums) # if k is bigger than length, use %  to ensure that it effectively reduces k to a smaller equivalent value the same result.
        nums[:] = nums[-k:] + nums[:-k]
        # nums[:] ensures that the changes are applied as original value
        # -k: means This slice notation gets the last k elements of the list.
        # :-k means This slice notation gets all elements of the list except the last k elements.
        return nums
nums = [1,2]
k = 3

print(rotate(nums, k))