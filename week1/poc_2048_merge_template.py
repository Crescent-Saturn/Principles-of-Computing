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
    	if l[i] != 0:
    		s1[j] = l[i]

    return []

a = [2,0,2,4]

print merge(a)