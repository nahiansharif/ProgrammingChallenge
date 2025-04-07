def merge(nums1, m, nums2, n):
    for i in range(0, n): 
        nums1[m + i] = nums2[i]
    print(nums1)
    for i in range(0, len(nums1)):
        for j in range(0, len(nums1)):
            if(nums1[i] < nums1[j]):
                temp = nums1[i]
                nums1[i] = nums1[j]
                nums1[j] = temp
    
    print(nums1)
    












nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3


merge(nums1, m, nums2, n)