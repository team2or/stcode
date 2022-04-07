#영역 구하기
from sys import stdin
from collections import deque
m,n,k = map(int, stdin.readline().split())
dy=[-1,1,0,0]
dx=[0,0,-1,1]
graph=[list([0]*n) for _ in range(m)]

for _ in range(k):
    x1,y1,x2,y2 = map(int, stdin.readline().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j]=-1
result=[]
for i in range(m):
    for j in range(n):
        if graph[i][j] is 0:
            cnt=1
            queue = deque([])
            queue.append([i,j])
            graph[i][j]=cnt

            while queue:
                y,x= queue.popleft()
                for k in range(4):
                    ny= y+dy[k]
                    nx= x+dx[k]

                    if 0 <= nx < n and 0 <= ny < m and graph[ny][nx] == 0:
                        graph[ny][nx]=1
                        queue.append([ny,nx])
                        cnt+=1

            result.append(cnt)
print(len(result))
result.sort()
for i in result:
    print(i,end=" ")