#해커랭크
#복습
#Weather Observation Station 20
#https://www.hackerrank.com/challenges/weather-observation-station-20/problem?isFullScreen=true
SELECT round(avg(tab1.LAT_N), 4) FROM (SELECT @row:=@row+1 AS 'row', S.LAT_N FROM STATION S, (SELECT @row:=0) R ORDER BY S.LAT_N) AS tab1, (SELECT count(*) AS "count" FROM STATION) AS tab2 WHERE tab1.row >= tab2.count/2 and tab1.row <= ((tab2.count/2)+1);

#새문제
#15 Days of Learning SQL
#https://www.hackerrank.com/challenges/15-days-of-learning-sql/problem?isFullScreen=true
#답안
#https://profailure.tistory.com/130
#https://ysyblog.tistory.com/208
SELECT s.submission_date, s_count.hacker_count, s_best.best_hacker, h.name
FROM submissions as s
JOIN ( -- 현재까지 매일 submission 하는 hackers
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
JOIN ( -- 각 날짜별 가장 많이 submission한 hacker 
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
#DFS/BFS
#복습
#타겟넘버
#https://programmers.co.kr/learn/courses/30/lessons/43165
def solution(numbers, target):
    answer = 0
    q = [[numbers[0],0],[-1*numbers[0],0]]
    n = len(numbers)
    while q:
        temp, idx = q.pop()
        idx += 1
        if idx < n:
            q.append([numbers[idx]+temp, idx])
            q.append([numbers[idx]+temp, idx])
        else:
            if temp == target:
                answer += 1
    return answer
    

