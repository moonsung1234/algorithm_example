
from typing import SupportsFloat


def solveMaze(maze, start, end) :
    queue = []
    done = set()

    queue.append(start)
    done.add(start)

    while queue :
        p = queue.pop(0)
        v = p[-1]

        if v == end :
            return p

        for x in maze[v] :
            if x not in done :
                queue.append(p + x)
                done.add(x)

    return -1 # not found

maze = {
    "a" : ["e"],
    "b" : ["c", "f"],
    "c" : ["b", "d"],
    "d" : ["c"],
    "e" : ["a", "i"],
    "f" : ["b", "g", "j"],
    "g" : ["f", "h"],
    "h" : ["g", "l"],
    "i" : ["e", "m"],
    "j" : ["f", "k", "n"],
    "k" : ["j", "o"],
    "l" : ["h", "p"],
    "m" : ["i", "n"],
    "n" : ["m", "j"],
    "o" : ["k"],
    "p" : ["l"]
}

print(solveMaze(maze, "a", "p"))