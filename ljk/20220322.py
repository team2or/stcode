#연결 요소의 개수
from sys import stdin
class ans:
    def __init__(self):
        self.solution()

    def solution(self):
        n, m= map(int, stdin.readline().split())
        arr=[[] for _ in range(n+1)]
        for _ in range(m):
            x,y = map(int, stdin.readline().split())
            arr[x].append(y)
            arr[y].append(x)
        self.result=[0]*(n+1)
        answer=0
        for i,j in enumerate(arr):
            if self.result[i]==0:
                self.result[i]=1
            for k in j:
                self.bang(k)

    def bang(self, num):
        while self.result[num]:
            self.result[num].pop(0)



if __name__=="__main__":
    ans()
