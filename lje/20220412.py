#해커랭크
#복습
#Occupations
#https://www.hackerrank.com/challenges/occupations/problem?isFullScreen=true
SELECT
MAX(CASE WHEN Occupation = "Doctor" THEN Name END),
MAX(CASE WHEN Occupation = "Professor" THEN Name END),
MAX(CASE WHEN Occupation = "Singer" THEN Name END),
MAX(CASE WHEN Occupation = "Actor" THEN Name END)
FROM (SELECT *, row_number() OVER (PARTITION BY Occupation ORDER BY Name) rn FROM OCCUPATIONS) t GROUP BY rn;
#[참고]
#https://sg-moomin.tistory.com/m/entry/%EC%84%B8%EB%AC%B4%EB%AF%BC%EC%9D%98-%EC%BD%94%EB%94%A9%EC%9D%BC%EA%B8%B0-mysql%EC%97%90%EC%84%9C-%ED%94%BC%EB%B2%97-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0

#프로그래머스
#DFS/BFS
#네트워크
#https://programmers.co.kr/learn/courses/30/lessons/43162
from collections import deque               
def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            queue = deque([i])
            visited[i] = True
            while queue:
                v = queue.popleft()
                for j in range(n):
                    if not visited[j] and computers[v][j] == 1:
                        queue.append(j)
                        visited[j] = True
            answer += 1

    return answer

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])
solution(4, [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1]])

#[참고]
#https://hwisaek.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-Python
