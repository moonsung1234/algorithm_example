
def findMax(a) :
    n = len(a)
    max_v = a[0]
    
    for i in range(1, n) :
        if a[i] > max_v :
            max_v = a[i]

    return max_v

def findMaxIndex(a) :
    n = len(a)
    max_index = 0

    for i in range(1, n) :
        if a[i] > a[max_index] :
            max_index = i

    return max_index

a = [17, 92, 18, 23, 45, 65, 77, 90]

print(findMax(a))
print(findMaxIndex(a))

