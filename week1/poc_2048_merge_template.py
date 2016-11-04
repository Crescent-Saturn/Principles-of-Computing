"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    s1 = []
    for i in line:
    	if i != 0:
    		s1.append(i)
    for i in line:
    	if i == 0:
    		s1.append(i)
    return []
