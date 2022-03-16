#백설 공주와 일곱 난쟁이

import sys
def solution():
    hats = [int(sys.stdin.readline()) for _ in range(9)]
    total= sum(hats)
    TF=False
    
    for i in range(9):
        for j in range(i+1,9):
            if total - hats[i]-hats[j]==100:
                hats.pop(j)
                hats.pop(i)
                hats.sort()
                return hats

if __name__=="__main__":
    hats=solution()
    for hat in hats:
        print(hat)
