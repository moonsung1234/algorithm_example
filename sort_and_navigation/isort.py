
# 삽입 정렬

def isort(a) :
    n = len(a)

    for i in range(1, n) :
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key :
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a

a = [3, 5, 1, 2, 7, 6]

print(isort(a))