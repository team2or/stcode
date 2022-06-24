#해커랭크
#15Days of Learning SQL
#답안: https://profailure.tistory.com/130
#현재까지 매일 submission하는 hackers 카운트
SELECT submission_date, count(DISTINCT hacker_id) as hacker_cnt FROM Submissions S1
WHERE submission_date - DATE("2016-03-01") = (SELECT count(DISTINCT submission_date) FROM Submissions S2
                                             WHERE S2.submission_date < S1.submission_date AND S2.hacker_id=S1.hacker_id) GROUP BY submission_date;

#각 날짜별 가장 많이 submission한 hacker
SELECT submission_date, hacker_id as best_hacker FROM submissions as s3
WHERE hacker_id = (SELECT hacker_id FROM submissions as s4
WHERE s4.submission_date = s3.submission_date GROUP BY hacker_id ORDER BY count(submission_id) desc, hacker_id limit 1)GROUP BY submission_date, hacker_id;

#답
#매일 submission하는 hacker 수와 각 날짜별 가장 많이 submission한 hacker의 id와 name을 출력하는 문제
SELECT s.submission_date, s_count.hacker_count, s_best.best_hacker, h.name
FROM submissions as s
JOIN (
    SELECT submission_date, count(distinct hacker_id) as hacker_count
    FROM submissions as s1
    WHERE submission_date - DATE('2016-03-01') = (
        SELECT count(distinct submission_date)
        FROM submissions as s2
        WHERE s2.submission_date < s1.submission_date
        and s2.hacker_id = s1.hacker_id
        )
    GROUP BY submission_date
    ) as s_count on s.submission_date = s_count.submission_date
JOIN (
    SELECT submission_date, hacker_id as best_hacker
    FROM submissions as s3
    WHERE hacker_id = (
        SELECT hacker_id
        FROM submissions as s4
        WHERE s4.submission_date = s3.submission_date
        GROUP BY hacker_id
        ORDER BY count(submission_id) desc, hacker_id limit 1
        )
    GROUP BY submission_date, hacker_id
    ) as s_best on s.submission_date = s_best.submission_date
JOIN hackers as h on s_best.best_hacker = h.hacker_id
GROUP BY s.submission_date, s_count.hacker_count, s_best.best_hacker, h.name
ORDER BY s.submission_date;


#프로그래머스
#폰켓몬
#https://programmers.co.kr/learn/courses/30/lessons/1845
nums = [3,1,2,3]
nums = [3,3,3,2,2,4]
nums = [3,3,3,2,2,2]
c = int(len(nums)/2)
nums_cnt = len(set(nums))
if c < nums_cnt:
    print(c)
else:
    print(nums_cnt)

#다른 답안
def solution(ls):
    #둘 중 작은 값을 출력하도록 min()함수 이용
    return min(len(ls)/2, len(set(ls)))
