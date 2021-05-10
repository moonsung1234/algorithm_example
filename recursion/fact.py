
def fact1(n) :
    f = 1

    for i in range(1, n + 1) :
        f *= i

    return f

def fact2(n) :
    if n <= 1 :
        return 1

    return n * fact2(n - 1)

print(fact1(3))
print(fact2(3))