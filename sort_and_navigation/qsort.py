
# 퀵 정렬

def qsort_sub(a, start, end) :
    if end - start <= 0 :
        return

    pivot = a[end]
    i = start

    for j in range(start, end) :
        if a[j] <= pivot :
            a[i], a[j] = a[j], a[i]
            i += 1
        
    a[i], a[end] = a[end], a[i]

    qsort_sub(a, start, i - 1)
    qsort_sub(a, i + 1, end)

    return a

def qsort(a) :
    return qsort_sub(a, 0, len(a) - 1)

a = [3, 4, 6, 1, 2, 9, 8, 7, 10]

print(qsort(a))