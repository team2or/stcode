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

#프로그래머스
#BFS
#단어 변환
#https://programmers.co.kr/learn/courses/30/lessons/43163
from collections import deque
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

def solution(begin,target, words):
    q = deque([(begin,0)])
    visited = [0 for _ in range(len(words))]
    if target not in words:
        return 0
    while q:
        now, cnt = q.popleft()
        if now == target:
            return cnt
        for i in range(len(words)):
            temp_cnt = 0
            if not visited[i]:
                for j in range(len(now)):
                    if now[j] != words[i][j]:
                        temp_cnt += 1
                if temp_cnt == 1:
                    q.append((words[i], cnt+1))
                    visited[i] = 1

print(solution(begin, target, words))

#다른답안
#https://velog.io/@op032/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8B%A8%EC%96%B4-%EB%B3%80%ED%99%98python
from collections import deque
def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])
    V = [ 0 for i in range(len(words))]
    while q:
        word, cnt = q.popleft()
        if word == target:
            answer = cnt
            break        
        for i in range(len(words)):
            temp_cnt = 0
            if not V[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        temp_cnt += 1
                if temp_cnt == 1:
                    q.append([words[i], cnt+1])
                    V[i] = 1
                    
    return answer

print(solution(begin, target, words))