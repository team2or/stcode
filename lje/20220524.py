#해커랭크
#복습
#Contest Leaderboard
#https://www.hackerrank.com/challenges/contest-leaderboard/problem?isFullScreen=true
SELECT tab1.hacker_id, H.name, sum(tab1.max_score) FROM (SELECT hacker_id, challenge_id, max(score) as max_score FROM Submissions GROUP BY challenge_id, hacker_id) tab1 LEFT JOIN Hackers H ON tab1.hacker_id=H.hacker_id GROUP BY tab1.hacker_id, H.name HAVING sum(tab1.max_score) > 0 ORDER BY sum(tab1.max_score) DESC, tab1.hacker_id;

#프로그래머스
#완전탐색
#모음사전
#https://programmers.co.kr/learn/courses/30/lessons/84512
from itertools import product
def solution(word):
    dict = []
    #모든 조합을 생성
    for i in range(1,6):
        dict += list(map(''.join, product("AEIOU", repeat=i)))
    #알파벳순으로 정렬
    dict.sort()
    answer = dict.index(word) + 1

    return answer
