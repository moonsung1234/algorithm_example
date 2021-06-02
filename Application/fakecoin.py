
def weigh(a, b, c, d) :
    fake = 29

    if a <= fake and fake <= b :
        return -1

    elif c <= fake and fake <=d :
        return 1

    return 0

def findFakeCoin1(left, right) :  
    for i in range(left + 1, right + 1) :
        result = weigh(left, left, i, i)

        if result == -1 :
            return left

        elif result == 1 :
            return i

    return -1

def findFakeCoin2(left, right) :
    if left == right :
        return left

    half = (right - left + 1) // 2
    left1 = left
    right1 = left + half - 1
    left2 = left + half
    right2 = left2 + half - 1

    result = weigh(left1, right1, left2, right2)

    if result == -1 :
        return findFakeCoin2(left1, right1)

    elif result == 1 :
        return findFakeCoin2(left2, right2)

    return right
    

n = 100

print(findFakeCoin1(0, n - 1))
print(findFakeCoin2(0, n - 1))