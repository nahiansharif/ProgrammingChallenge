def shiftingString(s, leftShift, rightShift):
    char = []
    
    for i in range(len(s)): 
        char.append(s[i])
    
    
    n = len(char) - 1
    i = 0
    while i < leftShift:
        temp = char[0]
        char.pop(0)
        char.append(temp)
        i += 1
    
    i = 0
    while i < rightShift:
        temp = char[n]
        char.pop(n)
        char.insert(0, temp)
        i += 1
    
    print(''.join(char))
    
s = "abcdefg"
left = 2
right = 4

shiftingString(s, left, right)