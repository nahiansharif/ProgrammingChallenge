#
# 

def romanNum(s):    

    char = list(s)
    num = 0
    romanDict = {
        "M":1000,
        "D":500,
        "C":100,
        "L":50,
        "X":10,
        "V":5,
        "I":1,
        "CM":900,
        "CD":400,
        "XC":90,
        "XL":40,
        "IX":9,
        "IV":4,
    }
    char = list(s)
    num = 0
    for i in range (1, len(char)):
        if char[i - 1] + char[i] in romanDict:
            num += romanDict[char[i - 1] + char[i]]
            char[i - 1] = " "
            char[i] = " "
    for i in range (0, len(char)):
        if char[i] in romanDict:
            num += romanDict[char[i]]
            char[i] = " "
    return num

s = "MCDXXVII" # 1427
print(romanNum(s))

s = "MCMXCIV" # 1994
print(romanNum(s))

s = "II" # 1994
print(romanNum(s))