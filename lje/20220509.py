#해커랭크
#복습
#Occupations
#https://www.hackerrank.com/challenges/occupations/problem?isFullScreen=true
#row_number()을 partition by로 직업별로 묶고 Name 순으로 정렬한 데이터에 적용
#그리고 row_number()로 각 직업별 1번부터 차례로 출력하기 위해 row_number()를 GROUP BY함
#GROUP BY하기 위해서는 집계함수 사용해야 하므로 max 사용
SELECT
max(CASE WHEN Occupation="Doctor" THEN Name END),
max(CASE WHEN Occupation="Professor" THEN Name END),
max(CASE WHEN Occupation="Singer" THEN Name END),
max(CASE WHEN Occupation="Actor" THEN Name END) FROM
(SELECT *, row_number() over (PARTITION BY Occupation ORDER BY Name) rn FROM OCCUPATIONS) t
GROUP BY rn;


#프로그래머스
#땅따먹기
#https://programmers.co.kr/learn/courses/30/lessons/12913
#내 답안 테스트케이스만 통과
#모든열에서 최대값을 찾아 더하는게 아니라
#최종합이 최대가 되는 수를 구하는 것
#만약 [[1,1,99,100],[1,1,1,99]]일 때 99+99인 198이 최대가 되어야 함
land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
land = [[1,1,99,100],[1,1,1,99]]
answer = 0
ex_index = 4
for lan in land:
    max_num = max(lan)
    num_index = lan.index(max_num)
    if answer == 0 and ex_index == 4:
        answer += max_num
        ex_index = num_index
    elif num_index == ex_index:
        max_num = sorted(lan)[2]
        ex_index = lan.index(max_num)
        answer += max_num
    else:
        answer += max_num
        ex_index = num_index
print(answer)

#답안
#https://programmers.co.kr/learn/courses/18/lessons/846#
#https://eda-ai-lab.tistory.com/480
#동적,다이나믹 프로그래밍(dp알고리즘)
#이전행의 최대값을 더함(이전행에서 같은 열 제외)
land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
land = [[1,1,99,100],[1,1,1,99]]
for i in range(0, len(land)-1):
    land[i+1][0] += max(land[i][1],land[i][2],land[i][3])
    land[i+1][1] += max(land[i][0],land[i][2],land[i][3])
    land[i+1][2] += max(land[i][0],land[i][1],land[i][3])
    land[i+1][3] += max(land[i][0],land[i][1],land[i][2])
    print(land)
print(max(land[-1]))

#다른답안
for i in range(1, len(land)):
    for j in range(len(land[0])):
        land[i][j] += max(land[i-1][:j]+land[i-1][j+1:])
print(max(land[-1]))