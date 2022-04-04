#해커랭크
#복습
#Challenges
#https://www.hackerrank.com/challenges/challenges/problem?isFullScreen=true
SELECT C.hacker_id, H.name, count(C.hacker_id) as challenges_created FROM Challenges C LEFT JOIN Hackers H ON C.hacker_id = H.hacker_id
GROUP BY C.hacker_id, H.name
HAVING challenges_created = (SELECT count(hacker_id) AS challenge_max FROM Challenges GROUP BY hacker_id ORDER BY challenge_max DESC LIMIT 1)
OR
challenges_created IN (SELECT sub1.challenges_created FROM (SELECT count(*) as challenges_created FROM Challenges GROUP BY hacker_id) sub1  GROUP BY sub1.challenges_created HAVING count(*) = 1) ORDER BY challenges_created DESC, C.hacker_id;

#새문제
#Print Prime Numbers
#https://www.hackerrank.com/challenges/print-prime-numbers/problem?isFullScreen=true
#답안
#https://www.hackerrank.com/challenges/print-prime-numbers/forum
SET @potential_prime = 1;
SET @divisor = 1;

SELECT GROUP_CONCAT(POTENTIAL_PRIME SEPARATOR '&') FROM
    (SELECT @potential_prime := @potential_prime + 1 AS POTENTIAL_PRIME FROM
    information_schema.tables t1,
    information_schema.tables t2
    LIMIT 1000) list_of_potential_primes
WHERE NOT EXISTS(
	SELECT * FROM
        (SELECT @divisor := @divisor + 1 AS DIVISOR FROM
	    information_schema.tables t1,
        information_schema.tables t2
	    LIMIT 1000) list_of_divisors
	WHERE MOD(POTENTIAL_PRIME, DIVISOR) = 0 AND POTENTIAL_PRIME <> DIVISOR);

#[참고]
#<>연산자 같지 않음
#https://docs.microsoft.com/ko-kr/sql/t-sql/language-elements/comparison-operators-transact-sql?view=sql-server-ver15
#MOD함수 두수의 나머지를 반환
#https://goyunji.tistory.com/123
#information_schema.tables: DB에 있는 임시 데이터베이스 1000개 이하여서 2개를 사용
#다른 답안
#https://techblog-history-younghunjo1.tistory.com/173

#프로그래머스
#스택/큐
#주식가격
#https://programmers.co.kr/learn/courses/30/lessons/42584
#prices리스트를 deque로 변환하지 않으면 효율성에서 시간초과로 실패됨
#
from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        price = prices.popleft()
        count = 0
        for p in prices:
            count += 1
            if price > p:
                break
        answer.append(count)
    
    return answer
solution([1, 2, 3, 2, 3])
solution([1, 2, 3, 2, 3, 1])

#[참고]
#https://velog.io/@soo5717/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A3%BC%EC%8B%9D%EA%B0%80%EA%B2%A9-Python