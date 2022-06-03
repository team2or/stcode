#해커랭크
#복습
#Top Competitors
#https://www.hackerrank.com/challenges/full-score/problem?isFullScreen=true
SELECT H.hacker_id, H.name FROM (SELECT S.hacker_id, count(hacker_id) as cnt FROM Submissions S LEFT JOIN (SELECT C.challenge_id, D.score FROM Challenges C LEFT JOIN Difficulty D ON C.difficulty_level=D.difficulty_level) CD ON S.challenge_id=CD.challenge_id WHERE S.score = CD.score GROUP BY S.hacker_id) tab1 LEFT JOIN Hackers H ON tab1.hacker_id = H.hacker_id WHERE tab1.cnt > 1 ORDER BY tab1.cnt DESC, H.hacker_id;

#나는 계속 2개씩 join을 해서 결과값을 가지고 또 join하고 하는 방식으로 풀었는데 다른 답안은 Inner JOIN으로 한번에 조인을 한 후에 Having으로 count한 조건을 처리함 이게 훨씬 덜 복잡하고 보기 편한 방식 같다.
#다른답안
#https://hanawithdata.tistory.com/entry/%ED%95%B4%EC%BB%A4%EB%9E%AD%ED%81%AC-Top-Competitors
SELECT s.hacker_id, h.name
FROM Submissions s
    INNER JOIN Challenges c ON s.challenge_id = c.challenge_id
    INNER JOIN Difficulty d ON c.difficulty_level = d.difficulty_level
    INNER JOIN Hackers h ON s.hacker_id = h.hacker_id
WHERE d.score = s.score
GROUP BY s.hacker_id, h.name
HAVING count(s.challenge_id) > 1
ORDER BY count(s.challenge_id) DESC, s.hacker_id

#프로그래머스
#줄 서는 방법
#https://programmers.co.kr/learn/courses/30/lessons/12936
