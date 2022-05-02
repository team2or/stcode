#해커랭크
#복습
#The Report
#https://www.hackerrank.com/challenges/the-report/problem?isFullScreen=true
#BETWEEN AND로 JOIN ON하기
#JOIN하기 위한 컬럼이 똑같지 않으므로 조건사이에 해당하면 JOIN하는 식으로 JOIN
SELECT CASE WHEN G.Grade < 8 THEN NULL ELSE S.Name END as Name, G.Grade, S.Marks FROM Students S JOIN Grades G ON S.Marks BETWEEN G.Min_Mark AND G.Max_Mark ORDER BY G.Grade DESC, S.Name, S.Marks;

#프로그래머스
#탐욕법/가장작은
#구명보트
#https://programmers.co.kr/learn/courses/30/lessons/42885
people = [70,50,80,50]
limit = 100
people.sort()
cnt = 0
while people:
    if len(people) > 2:
        if people[0]+people[1] <= limit:
            people.pop(0)
            people.pop(0)
            cnt += 1
        else:
            people.pop(0)
            cnt += 1
    else:
        people.pop()
        cnt += 1
print(cnt)

#답안
#https://velog.io/@daon9apples/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level-2-%EA%B5%AC%EB%AA%85%EB%B3%B4%ED%8A%B8-python
people = [70,50,80,50]
limit = 100
from collections import deque #안쓰면 시간초과뜸
people.sort()
people = deque(people)
cnt = 0
while people:
    #보트에는 최대 2명씩 밖에 못탐
    if len(people) >= 2:
        #두명의 무게가 최대무게보다 적을 때
        if people[0]+people[-1] <= limit:
            people.pop()
            people.popleft()
            cnt += 1
        #두명의 무게가 최대무게 초과일 때
        #무거운 사람부터 태워보냄
        elif people[0]+people[-1] > limit:
            people.pop()
            cnt += 1
    #마지막 한명만 남았을 때
    else:
        people.pop()
        cnt += 1
print(cnt)

#다른답안
#https://leedakyeong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B5%AC%EB%AA%85%EB%B3%B4%ED%8A%B8-in-python
people = [70,50,80,50]
limit = 100
people.sort()
cnt = 0
start, end = 0, len(people)-1
while start <= end:
    cnt += 1
    if people[start]+people[end]<=limit:
        start += 1
    end -= 1
print(cnt)