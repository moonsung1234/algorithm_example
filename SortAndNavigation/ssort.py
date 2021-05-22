
# 선택 정렬

def ssort(a) :
    n = len(a)

    for i in range(n - 1) :
        min_index = i

        for j in range(i + 1, n) :
            if a[j] < a[min_index] :
                min_index = j
        
        a[i], a[min_index] = a[min_index], a[i]

    return a

a = [10, 3, 4, 1, 2, 5, 8, 6, 9, 0]

print(ssort(a))