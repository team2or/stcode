#백설 공주와 일곱 난쟁이

import sys
def solution():
    hats = []
    for i in range(9):
        hats.append(int(sys.stdin.readline()))
    hats.sort(reverse=True)
     if sum(hats[:8]) 100:
        return hats[:8]



