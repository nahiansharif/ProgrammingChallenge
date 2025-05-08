# prepare for the interview question
# remember, you failed miserably in paycom interview, but you have 6 months until july to make a great comback. 

nums = [1, 2, 3, 4, 5, 8, 9, 11, 15]
target  = 6

left, right = 0, len(nums)-1

while left <= right:
    mid = len(nums)//2

    if nums[mid] == target:
        print(mid)
    elif nums[left] < target:
        left = mid + 1
    else:
        right = mid- 1

print(left)

