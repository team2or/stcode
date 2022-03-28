#토마토
from sys import stdin
from collections import deque
class Tomato:
    def __init__(self):
        m,n = map(int, stdin.readline().split())
        tomatos=[list(map(int, stdin.readline().split())) for _ in range(n)]
        queue= deque([])
        dx, dy= [-1,1,0,0],[0,0,-1,1]
        answer=0

        for i in range(n):
            for j in range(m):
                if tomatos[i][j]==1:
                    queue.append([i,j])
        self.bfs(queue,dx,dy, tomatos,n,m)
        for i in tomatos:
            for j in i:
                if j==0:
                    print(-1)
                    exit(0)
            answer=max(answer, max(i))
        print(answer-1)

    def bfs(self, queue,dx, dy, tomatos,n,m):
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx, ny = dx[i]+x, dy[i]+y
                if 0<= nx <n and 0<= ny< m and tomatos[nx][ny]==0:
                    tomatos[nx][ny]=tomatos[x][y]+1
                    queue.append([nx,ny])




if __name__=="__main__":
    Tomato()
