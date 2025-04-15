a, b = 5, 2

print(a + b)   # 7
print(a - b)   # 3
print(a * b)   # 10
print(a / b)   # 2.5
print(a // b)  # 2
print(a % b)   # 1
print(a ** b)  # 25


# max int
x = float("inf")
print(x)

# min int
x = float("-inf")
print(x)


ss = "abc"
s = [i for i in ss]
s[1] = "x"
ss = "".join(s)
print(ss)

# Assignment Operators: +=, -=, *=, /=, //=, %=, **=

x = 10
x += 3  # x becomes 13
x //= 2 # x becomes 6

abs(-10)  # 10
round(3.1415, 2)  # 3.14


min(1, 2, 3)  # 1
max(1, 2, 3)  # 3

sum([1, 2, 3])  # 6


pow(2, 3)  # 8, same as 2**3

import math

print(math.sqrt(16))     # 4.0
print(math.floor(3.7))   # 3
print(math.ceil(3.2))    # 4
print(math.gcd(12, 18))  # 6
print(math.isqrt(10))    # 3
print(math.factorial(5)) # 120

# Count Digits
num = 1234
count = 0
while num:
    count += 1
    num //= 10
    
n = 123
rev = 0
while n:
    rev = rev * 10 + n % 10
    n //= 10

n = 123
rev = 0
while n:
    rev = rev * 10 + n % 10
    n //= 10


