# Problem: Given an array of integers, find the length of the longest subarray whose sum equals k.
# Example Input: nums = [1, -1, 5, -2, 3], k = 3
# Example Output: 4

def longest_subarray_with_sum_k(nums, k):
    sum_indices = {}
    current_sum = 0
    max_length = 0

    for i in range(len(nums)):
        current_sum += nums[i]
        # print(current_sum)

        if current_sum == k:
            max_length = i + 1
            print("olamalaka")
        if current_sum - k in sum_indices:
            max_length = max(max_length, i - sum_indices[current_sum - k])
            print("                         chagol")

        if current_sum not in sum_indices:
            sum_indices[current_sum] = i
            print("kukur")


    
    for key, value in sum_indices.items():
        print(key, value)

    return max_length

# Example usage
nums = [1, -1, 5, -2, 3]
k = 3
print(longest_subarray_with_sum_k(nums, k))  # Output: 4
print(" ")
nums = [5, -1, 5, -2, 3, 7, 2, 3, 5, 8]
k = 13
print(longest_subarray_with_sum_k(nums, k))  # Output: 5
