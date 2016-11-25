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

    for k in range(l-1):
        if s1[k] == s1[k+1]:
            s1[k] *=2
            s1.pop(k+1)
            s1.append(0)


    return s1

a = [2,2,2,2]

print (merge(a))