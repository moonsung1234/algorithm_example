
# 선택 정렬

def findMinIndex(a) :
    n = len(a)
    min_index = 0

    for i in range(n) :
        if a[i] < a[min_index] :
            min_index = i

    return min_index

def ssort(a) :
    result = []

    while a :
        min_index = findMinIndex(a)
        value = a.pop(min_index)
        
        result.append(value)

    return result

a = [3, 4, 1, 2, 5, 8, 6, 9, 0]

print(ssort(a))