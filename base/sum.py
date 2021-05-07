
def sum1(n) :
    s = 0

    for i in range(1, n + 1) :
        s += i

    return s

def sum2(n) :
    return n * (n + 1) / 2

def sumSquare1(n) :
    s = 0
    
    for i in range(1, n + 1) :
        s += i ** 2

    return s

def sumSquare2(n) :
    return n * (n + 1) * (2 * n + 1) / 6

print(sum1(10))
print(sum2(10))
print(sumSquare1(10))
print(sumSquare2(10))
