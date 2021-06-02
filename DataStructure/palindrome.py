
def checkPalindrome(_str) :
    queue = [] # FIFO : First In First Out
    stack = [] # LIFO : Last In First Out

    for s in _str :
        if s.isalpha() :
            queue.append(s.lower())
            stack.append(s.lower())

    while queue and stack :
        if not queue.pop(0) == stack.pop() :
            return False

    return True

print(checkPalindrome("Wow"))
print(checkPalindrome("HelloWorld!"))


