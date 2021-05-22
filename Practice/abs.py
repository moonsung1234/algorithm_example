
import math

def abs1(a) :
    if a >= 0 :
        return a

    else :
        return -a

def abs2(a) :
    b = a * a

    return math.sqrt(b)

print(abs1(4))
print(abs2(4))

print(abs1(-5))
print(abs2(-5))
