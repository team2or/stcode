#해커랭크
#Interviews
#https://www.hackerrank.com/challenges/interviews/problem?isFullScreen=true
#View_Stats와 Submission_Stats 테이블의 challenge_id 기준 각 컬럼의 합을 먼저 구함
SELECT challenge_id, sum(total_views), sum(total_unique_views) FROM View_Stats GROUP BY challenge_id;
SELECT challenge_id, sum(total_submissions), sum(total_accepted_submissions) FROM Submission_Stats GROUP BY challenge_id;
#모든 테이블 JOIN 후 contest_id로 GROUP BY
SELECT Con.contest_id, Con.hacker_id, Con.name, sum(total_submissions), sum(total_accepted_submissions), sum(V.total_views), sum(V.total_unique_views) FROM Contests Con LEFT JOIN Colleges Col ON Con.contest_id = Col.contest_id
LEFT JOIN Challenges Chal ON Col.college_id = Chal.college_id
LEFT JOIN (SELECT challenge_id, sum(total_views) as total_views, sum(total_unique_views) as total_unique_views FROM View_Stats GROUP BY challenge_id) AS V ON Chal.challenge_id = V.challenge_id
LEFT JOIN (SELECT challenge_id, sum(total_submissions) as total_submissions, sum(total_accepted_submissions) as total_accepted_submissions FROM Submission_Stats GROUP BY challenge_id) S ON Chal.challenge_id = S.challenge_id GROUP BY Con.contest_id, Con.hacker_id, Con.name
#모든 sums의 합이 0이면 제외 후 contest_id 정렬
SELECT Con.contest_id, Con.hacker_id, Con.name, sum(total_submissions), sum(total_accepted_submissions), sum(V.total_views), sum(V.total_unique_views) FROM Contests Con LEFT JOIN Colleges Col ON Con.contest_id = Col.contest_id
LEFT JOIN Challenges Chal ON Col.college_id = Chal.college_id
LEFT JOIN (SELECT challenge_id, sum(total_views) as total_views, sum(total_unique_views) as total_unique_views FROM View_Stats GROUP BY challenge_id) AS V ON Chal.challenge_id = V.challenge_id
LEFT JOIN (SELECT challenge_id, sum(total_submissions) as total_submissions, sum(total_accepted_submissions) as total_accepted_submissions FROM Submission_Stats GROUP BY challenge_id) S ON Chal.challenge_id = S.challenge_id GROUP BY Con.contest_id, Con.hacker_id, Con.name 
HAVING SUM(S.TOTAL_SUBMISSIONS) + SUM(S.TOTAL_ACCEPTED_SUBMISSIONS) + SUM(V.TOTAL_VIEWS) + SUM(V.TOTAL_UNIQUE_VIEWS) > 0 ORDER BY Con.contest_id;

#[참고]
#https://yurimyurim.tistory.com/13
#https://ysyblog.tistory.com/207

#백준
#BFS
#반복수열
#https://www.acmicpc.net/problem/2331
a, p = map(int, input().split())

nums = [a]
while True:
    new = 0
    for i in str(nums[-1]):
        new += int(i)**p
    if new in nums:
        break
    else:
        nums.append(new)
print(nums.index(new))


