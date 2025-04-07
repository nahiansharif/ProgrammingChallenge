def lonelyinteger(a):
    dict = {}
    
    for num in a:
        dict[num] = dict.get(num, 0) + 1
        
    for nums, count in dict.items(): 
        if count == 1:
            return nums
    
    
a = [1, 2, 3, 4, 3, 2, 1]

print(lonelyinteger(a))