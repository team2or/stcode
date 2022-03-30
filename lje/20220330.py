#해커랭크
#Binary Tree Nodes
#https://www.hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true
#답안
#https://velog.io/@develop_wan/MS-SQL-%ED%95%B4%EC%BB%A4%EB%9E%AD%ED%81%ACHacker-Rank-Binary-Tree-Nodes
SELECT N, CASE WHEN P IS NULL THEN 'Root'
WHEN N IN (SELECT DISTINCT P FROM BST) THEN 'Inner'
ELSE 'Leaf' END FROM BST ORDER BY N;

#Contest Leaderboard
#https://www.hackerrank.com/challenges/contest-leaderboard/problem?isFullScreen=true
SELECT S.hacker_id, H.name, sum(S.score) as score FROM (SELECT hacker_id, challenge_id, max(score) as score FROM Submissions GROUP BY hacker_id, challenge_id ORDER BY hacker_id, challenge_id) S
JOIN Hackers H ON S.hacker_id=H.hacker_id GROUP BY S.hacker_id, H.name HAVING score > 0 ORDER BY score DESC, S.hacker_id;

#[해설]
#먼저 Submissions테이블에서 hacker_id, challenge_id, score을 정렬해서 출력해봄
SELECT hacker_id, challenge_id, score FROM Submissions ORDER BY hacker_id, challenge_id, score DESC;
#그 다음 hacker_id와 challenge_id GROUP BY해서 각 challenge중 최고 score 출력
SELECT hacker_id, challenge_id, max(score) as score FROM Submissions GROUP BY hacker_id, challenge_id ORDER BY hacker_id, challenge_id;
#그렇게 최고 score을 출력한 것을 테이블로 사용해서 Hackers테이블과 조인 후에 hacker_id, name으로 GROUP BY해서 각 challenge별 최고 점수 sum()함 그리고 HAVING으로 score가 0인 참가자는 제외시킴
#마지막으로 정렬조건에 따라 최고점수를 받은 해커순으로 내림차순, 동일점수일 땐 hacker_id로 오름차순으로 정렬함.

#백준
#해시
#듣보잡
#https://www.acmicpc.net/problem/1764
n,m = map(int,input().split())
ls = {}
for _ in range(n+m):
    p = input()
    if p in ls:
        ls[p] += 1
    else:
        ls[p] = 1

answer = []
for k, v in ls.items():
    if v == 2:
        answer.append(k)
print(len(answer))
print("\n".join(sorted(answer)))

#다른답안
#집합이용
#https://dojinkimm.github.io/problem_solving/2019/09/26/boj-1764-deutbo.html
n,m = map(int, input().split())
x = set([input() for i in range(n)])
y = set([input() for i in range(m)])

z = sorted(list(x&y))
print(len(z))
for i in z:
    print(i)