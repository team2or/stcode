#해커랭크
#복습
#Weather Observation Station 20
#https://www.hackerrank.com/challenges/weather-observation-station-20/problem?isFullScreen=true
#중간값 구하기
SELECT round(tab1.LAT_N, 4) FROM (SELECT @row:=@row+1 AS 'row', S.LAT_N FROM STATION S, (SELECT @row:=0) R ORDER BY S.LAT_N) AS tab1, (SELECT count(*) AS 'count' FROM STATION) AS tab2 WHERE tab1.row >= tab2.count/2 AND tab1.row <= ((tab2.count/2)+1);

#프로그래머스
#전력망을 둘로 나누기
#https://programmers.co.kr/learn/courses/30/lessons/86971
#답안: https://cseella.tistory.com/155
n = 4
wires = [[1,2],[2,3],[3,4]]
from collections import deque
def bfs(start, visited, line):
    q = deque([start])
    result = 1
    visited[start] = True
    while q:
        now = q.popleft()
        for i in line[now]:
            if visited[i] == False:
                result += 1
                q.append(i)
                visited[i] = True
    return result

def solution(n, wires):
    answer = n
    line = [[] for _ in range(n+1)]
    for w,i in wires:
        line[w].append(i)
        line[i].append(w)
    print(line)
    for start, not_visit in wires:
        visited = [False]*(n+1)
        visited[not_visit] = True
        result = bfs(start,visited,line)
        if abs(result - (n-result)) < answer:
            answer = abs(result-(n-result))
            if answer == 0:
                return answer
    return answer
solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])
solution(4, [[1,2],[2,3],[3,4]])
solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]])

