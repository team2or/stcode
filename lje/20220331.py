#해커랭크
#Weather Observation Station 20
#https://www.hackerrank.com/challenges/weather-observation-station-20/problem?isFullScreen=true

SELECT round(AVG(mid_vals),4) AS 'median' FROM (
 SELECT tab1.LAT_N AS 'mid_vals' FROM
  (
   SELECT @row:=@row+1 AS 'row', S.LAT_N
   FROM STATION AS S, (SELECT @row:=0) AS r
   ORDER BY S.LAT_N
  ) AS tab1,
  (
   SELECT COUNT(*) as 'count'
   FROM STATION
  ) AS tab2
  WHERE tab1.row >= tab2.count/2 and tab1.row <= ((tab2.count/2) +1)) AS tab3;

#참고
#mysql: 중앙값 구하기
#https://www.delftstack.com/ko/howto/mysql/mysql-median/
#row를 생성해 ORDER BY한 LAT_N값에 순서맵핑
(SELECT @row:=@row+1 AS 'row', S.LAT_NFROM STATION AS S, (SELECT @row:=0) AS rORDER BY S.LAT_N) AS tab1
#count로 LAT_N 개수 구함
(SELECT COUNT(*) as 'count'FROM STATION) AS tab2
#WHERE절로 중간.중앙 순서 구하기
WHERE tab1.row >= tab2.count/2 and tab1.row <= ((tab2.count/2) +1))
#중간값이 2개일 수 있으므로 추출한 값에서 avg()로 평균낸 후 round()로 소수점 4째자리까지 출력

#Top Competitors
#https://www.hackerrank.com/challenges/full-score/problem?isFullScreen=true
SELECT H.hacker_id, H.name FROM (SELECT S.hacker_id, count(*) AS pass_game FROM Submissions S LEFT JOIN Challenges C ON S.challenge_id = C.challenge_id LEFT JOIN Difficulty D ON C.difficulty_level = D.difficulty_level WHERE S.score = D.score GROUP BY hacker_id) Sub LEFT JOIN Hackers H ON Sub.hacker_id = H.hacker_id WHERE Sub.pass_game > 1 ORDER BY Sub.pass_game DESC, H.hacker_id;

#백준
#해시
#비밀번호 찾기
#https://www.acmicpc.net/problem/17219
n, m = map(int,input().split())
site = {}
for _ in range(n):
    s, p = map(str, input().split())
    site[s] = p

for _  in range(m):
    url = input()
    print(site[url])

#비밀번호 만들기
#https://www.acmicpc.net/problem/17218
s_list = [input() for _ in range(2)]
s_list.sort(reverse=True)

answer = []
for i in s_list[0]:
    if i in s_list[1]:
        answer.append(i)
print(''.join(answer))
