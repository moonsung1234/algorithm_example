
def searchList(a, x) :
    n = len(a)

    for i in range(n) :
        if x == a[i] :
            return i

    return -1

a = [1, 2, 3, 4, 5]

print(searchList(a, 1))