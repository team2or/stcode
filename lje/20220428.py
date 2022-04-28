#해커랭크
#복습
#Contest Leaderboard
#https://www.hackerrank.com/challenges/contest-leaderboard/problem?isFullScreen=true
SELECT H.hacker_id, H.name, sum(S.max_score) as total_score FROM (SELECT hacker_id, challenge_id, max(score) as max_score FROM Submissions GROUP BY hacker_id, challenge_id) S LEFT JOIN Hackers H ON S.hacker_id = H.hacker_id
GROUP BY H.hacker_id, H.name HAVING total_score > 0 ORDER BY total_score DESC, H.hacker_id;

#프로그래머스
#큰수만들기
#https://programmers.co.kr/learn/courses/30/lessons/42883
#조합이용
#3~10 시간초과
from ast import While
from itertools import combinations
def solution(number, k):
    numbers = list(number)
    answer = '0'
    for c in combinations(numbers, len(number)-k):
        c = ''.join(c)
        if int(answer) < int(c):
            answer = c
    return answer

#다른답안
#https://sanghyu.tistory.com/136
#https://gurumee92.tistory.com/162
#stack 이용
def solution(number, k):
    stack = []
    for num in number:
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    return "".join(stack[:len(stack)-k])
solution("1924",2)
solution("1231234",3)
solution("4177252841",4)