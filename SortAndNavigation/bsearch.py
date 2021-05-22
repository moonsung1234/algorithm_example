
def bsearch(a, x) :
    start = 0
    end = len(a) - 1

    while start <= end :
        mid = (start + end) // 2

        if x == a[mid] :
            return mid

        elif x > a[mid] :
            start = mid + 1

        else :
            end = mid - 1

    return -1

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(bsearch(a, 3))