import math

x = 6
a = 2
b = 8 
y = 7
base = 8

math.sqrt(x)         # Square root
math.ceil(x)         # Round up
math.floor(x)        # Round down
math.factorial(x)    # Factorial
math.gcd(a, b)       # Greatest common divisor
math.log(x, base)    # Logarithm
math.pow(x, y)       # Power (float)


from collections import Counter, defaultdict, deque, namedtuple

seq = [1, 3, 4, 2, 5, 1,2 ,3, 5,1 ,25, 8]

Counter(seq)              # Count frequency of elements
defaultdict(list/int/set) # Auto-initializing dicts
deque()                   # Fast queue/stack
deque.appendleft(x)       # Add to front
deque.pop()               # Remove from back
deque.popleft()           # Remove from front
namedtuple("Point", "x y")# Lightweight object-like tuple

import heapq
heap = [1, 3, 4, 2, 5, 1,2 ,3, 5,1 ,25, 8]
heapq.heappush(heap, x)       # Push to min-heap
heapq.heappop(heap)           # Pop min
heapq.heappushpop(heap, x)    # Push and pop
heapq.heapify(list)           # Turn list into heap

# Max heap (invert numbers)
heapq.heappush(heap, -x)

from itertools import permutations, combinations, product, accumulate
r = 11
permutations(seq, r)     # All orderings
combinations(seq, r)     # r-combinations
product(a, b)            # Cartesian product
accumulate(seq)          # Running total

from functools import lru_cache

@lru_cache(maxsize=None)  # Recursion + Memoization
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

import random
arr = seq.copy()
random.randint(a, b)      # Random int [a, b]
random.shuffle(arr)       # In-place shuffle
random.choice(arr)        # Random element

import string

string.ascii_lowercase    # 'abcdefghijklmnopqrstuvwxyz'
string.digits             # '0123456789'

# ✅ math

# ✅ collections (especially Counter, defaultdict, deque)

# ✅ heapq

# ✅ itertools

# ✅ bisect

# ✅ functools.lru_cache