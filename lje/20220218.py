# 프로그래머스_SQL
#오랜 기간 보호한 동물(2)
#https://programmers.co.kr/learn/courses/30/lessons/59411
SELECT A.ANIMAL_ID, A.NAME FROM ANIMAL_OUTS as A, ANIMAL_INS as B
WHERE A.ANIMAL_ID = B.ANIMAL_ID ORDER BY A.DATETIME - B.DATETIME DESC LIMIT 2;

#LEFT JOIN을 이용한 답안
#https://pearlluck.tistory.com/46
SELECT OUTS.ANIMAL_ID, OUTS.NAME
FROM ANIMAL_OUTS OUTS
LEFT OUTER JOIN ANIMAL_INS INS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
ORDER BY OUTS.DATETIME - INS.DATETIME DESC
LIMIT 2;

#INNER JOIN과 DATEDIFF(날짜계산함수) 사용답안
#https://codingspooning.tistory.com/entry/MySQL-%EB%82%A0%EC%A7%9C-%EB%B9%84%EA%B5%90-%EB%B0%8F-%EC%B0%A8%EC%9D%B4-%EA%B5%AC%ED%95%98%EA%B8%B0?category=987092
SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME
FROM ANIMAL_OUTS INNER JOIN ANIMAL_INS
ON ANIMAL_OUTS.ANIMAL_ID = ANIMAL_INS.ANIMAL_ID
ORDER BY DATEDIFF(ANIMAL_OUTS.DATETIME, ANIMAL_INS.DATETIME) DESC LIMIT 2


#DATETIME에서 DATE로 형 변환
#https://programmers.co.kr/learn/courses/30/lessons/59414

#참고
#https://brianshop.tistory.com/52
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') as 날짜 FROM ANIMAL_INS;


#백준
#그리디
#보석도둑
#https://www.acmicpc.net/problem/1202

#시간초과
#heapq모듈 이용해서 풀어야함.
n, k = map(int, input().split()) #보석개수, 가방개수
jew = [list(map(int, input().split())) for _ in range(n)] #보석무게, 가격
max_bags = [int(input()) for _ in range(k)] #가방에 담을 수 있는 최대무게

jew.sort(key=lambda x: (x[1], x[0]), reverse=True)
max_bags.sort()
answer = 0

while len(max_bags) != 0 or len(jew) != 0:
    for b in max_bags:
        if jew[0][0] <= b:
            answer += jew[0][1]
            max_bags.remove(b)
            jew.pop(0)

print(answer)


#수정 답안
import heapq
import sys #input()으로 입력 받으면 시간초과 발생할 수 있음

n, k = map(int, sys.stdin.readline().split()) #보석개수, 가방개수

jews = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
bags = [int(sys.stdin.readline()) for _ in range(k)] #가방에 담을 수 있는 최대무게

#오름차순정렬
jews.sort()
bags.sort()

answer = 0
temp = []

for b in bags:
    while jews and jews[0][0] <= b:
        heapq.heappush(temp, -jews[0][1])
        heapq.heappop(jews)

    if temp:
        answer += -heapq.heappop(temp)
print(answer)


