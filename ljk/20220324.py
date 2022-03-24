#케빈 베이컨의 6단계 법칙
from sys import stdin
from collections import deque
class Bacon:
    def __init__(self):
        n,m = map(int, stdin.readline().split())
        real= {i:[] for i in range(1,n+1)}
        for _ in range(m):
            x,y = map(int, stdin.readline().split())
            real[x].append(y)
            real[y].append(x)
        dic={}
        for num in range(1,n+1):
            dic[num]=self.bfs(num,n,real)
        result=sorted(dic.items(), key=lambda x: x[1])
        print(result[0][0])

    def bfs(self, num, n, real):
        bacon=[0]*(n+1)
        visited=[num]
        queue= deque()
        queue.append(num)
        while queue:
            k= queue.popleft()
            for i in real[k]:
                if i not in visited:
                    bacon[i]=bacon[k]+1
                    queue.append(i)
                    visited.append(i)
        return sum(bacon)



if __name__=="__main__":
    Bacon()
