#20220503
from collections import deque, Counter

N = 0
answer = 0
visited = []

def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt
    for j in range(N):
        if k >= dungeons[j][0] and  visited[j] == 0:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt +1, dungeons)
            visited[j] = 0

def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0]*N
    dfs(k, 0, dungeons)
    print(answer)
    return answer

solution(80, [[80,20],[50,40],[30,10]])