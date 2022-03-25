#순열 사이클
from sys import stdin
from collections import deque
class Cycle:
    def __init__(self):
        t= int(stdin.readline())
        for _ in range(t):
            n=int(stdin.readline())
            cycle=[0]+list(map(int,stdin.readline().split()))
            answer=0
            # visited=[1]+[0]*(n)
            #
            # for i in range(1,n+1):
            #     queue= deque([i])
            #     if (visited[i]==0):
            #         answer+=1
            #         visited[i]=1
            #     while queue:
            #         num=queue.popleft()
            #         num2=cycle[num]
            #         if visited[num2]==0:
            #             visited[num2]=1
            #             queue.append(num2)
            # print(answer)

            visited=[0]*(n+1)
            for i in range(1,n+1):
                if visited[i]==0:
                    answer+=self.bfs(i,visited, cycle)
            print(answer)

    def dfs(self,i,visited,cycle):
        visited[i]=1
        num=cycle[i]
        if visited[num]==0:
            self.dfs(num)

if __name__=="__main__":
    Cycle()
