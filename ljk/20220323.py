#토마토
from sys import stdin
from collections import deque
class Tomato:
    def __init__(self):
        m,n = map(int, stdin.readline().split())
        tomatos=[list(map(int, stdin.readline().split())) for _ in range(n)]
        queue= deque([])
        dx, xy= [-1,1,0,0],[0,0,-1,1]
        answer=0

        for i in range(n):
            for j in range(m):




if __name__=="__main__":
    Tomato()
