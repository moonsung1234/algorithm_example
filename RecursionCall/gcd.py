
def gcd1(a, b) :
    i = min(a, b)

    while True :
        if a % i == 0 and b % i == 0 :
            break

        i -= 1

    return i

def gcd2(a, b) :
    if b == 0 :
        return a

    return gcd2(b, a % b)

print(gcd1(4, 6))
print(gcd2(4, 6))

