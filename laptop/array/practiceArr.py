lst = [1, -9, -2, 7, 8, 3, 2, -4, 6, 6, 1, -8, 9, -1, 7, -8, 5]

# append extend insert pop remove clear copy index count sort sorted reverse set jump half flat shuffle filter map reduce swap absolute hashmap rotation ::-1  :: 
import itertools as it
import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    return not any(n%i == 0 for i in it.islice(it.count(2), math.floor(math.sqrt(n) - 1)))

def generatePrint(n):
    return list(filter(lambda x: is_prime(x), it.takewhile(lambda x: x < n, it.count(2))))
    
print(generatePrint(200))