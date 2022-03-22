#연결 요소의 개수
from sys import stdin
from collections import deque
import sys
sys.setrecursionlimit(10000)
class ans:
    def __init__(self):
        answer=self.solution()
        print(answer)
    def solution(self):
        n, m= map(int, stdin.readline().split())
        self.arr=[[] for _ in range(n+1)]
        for _ in range(m):
            x,y = map(int, stdin.readline().split())
            self.arr[x].append(y)
            self.arr[y].append(x)
        self.result=[0]*(n+1)
        answer=0
        for i in range(1, n+1):
            if self.result[i]==0:
                answer+=1
                self.bang(i)
        return answer
    # def bang(self, i):
    #     queue= deque(self.arr[i])
    #     self.result[i]=1
    #     while queue:
    #         v= queue.popleft()

    #         for h in self.arr[v]:
    #             if self.result[h]!=1:
    #                 queue.append(h)
    #                 self.result[h]=1

    def bang(self, i):
        self.result[i]=1
        for h in self.arr[i]:
            if self.result[h]==0:
                self.bang(h)




if __name__=="__main__":
    ans()
