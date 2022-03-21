#촌수계산
import sys
from collections import deque
n= int(sys.stdin.readline())
a,b= map(int, sys.stdin.readline().split())
m= int(sys.stdin.readline())
arr=[[] for _ in range(n+1)]
result= [0]*(n+1)
for _ in range(m):
    x,y= map(int, sys.stdin.readline().split())
    arr[x].append(y)
    arr[y].append(x)

def bfs(s):
    q= deque()
    visited = [0 for _ in range(n+1)]

    q.append(s)
    visited[s] = 1

    while q:
        x = q.popleft()

        for i in arr[x]:
            if visited[i]==0:
                visited[i]=1
                result[i] = result[x]+1
                q.append(i)

bfs(a)
if result[b] !=0 :
    print(result[b])
else:
    print(-1)