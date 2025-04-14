#round decimal division into integer to round it when you are handling negative numbers

print(int(-3 / 2))

# be consisitant with module operator with negative numbers
import math
print(-10 % 3) #logic error
print(math.fmod(-10, 3))

