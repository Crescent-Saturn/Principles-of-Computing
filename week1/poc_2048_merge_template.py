"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    l = len(line)
    s1 = [0]*l
    j = 0
    for i in range(l):
        if line[i] != 0:
            s1[j] = line[i]
            j += 1
    return s1

a = [2,0,2,4]

print (merge(a))