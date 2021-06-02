
def printAllFriends(a, start) :
    queue = []
    done = set()

    queue.append((start, 0))
    done.add(start)

    while queue :
        (p, q) = queue.pop(0)
        
        print(p, q)

        for x in a[p] :
            if x not in done :
                queue.append((x, q + 1))
                done.add(x)

a = {
    "What Do You Mean?" : ["Sorry", "Boyfriend"],
    "Sorry" : ["What Do You Mean?", "Boyfriend", "Yummy"],
    "Boyfriend" : ["What Do You Mean?", "Sorry"],
    "Yummy" : ["Sorry"],
    "A" : ["B"],
    "B" : ["A"]
}

printAllFriends(a, "Boyfriend")
print()
printAllFriends(a, "A")