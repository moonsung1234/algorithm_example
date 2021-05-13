
# 병합 정렬

def msort(a) :
    n = len(a)
    
    if n <= 1 :
        return

    mid = n // 2
    g1 = a[mid:]
    g2 = a[:mid]

    msort(g1)
    msort(g2)

    i1 = 0
    i2 = 0
    ia = 0

    while i1 < len(g1) and i2 < len(g2) :
        if g1[i1] < g2[i2] :
            a[ia] = g1[i1]
            i1 += 1
            ia += 1

        else :
            a[ia] = g2[i2]
            i2 += 1
            ia += 1

    while i1 < len(g1) :
        a[ia] = g1[i1]
        i1 += 1
        ia += 1

    while i2 < len(g2) :
        a[ia] = g2[i2]
        i2 += 1
        ia += 1

    return a

a = [2, 3, 1, 4, 7, 5, 8, 6, 9]

print(msort(a))
