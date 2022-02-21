# 프로그래머스_SQL
#없어진 기록 찾기
#https://programmers.co.kr/learn/courses/30/lessons/59042
SELECT A.ANIMAL_ID, A.NAME FROM ANIMAL_OUTS A
LEFT JOIN ANIMAL_INS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.ANIMAL_ID IS NULL ORDER BY A.ANIMAL_ID;

#있었는데요 없었습니다
#https://programmers.co.kr/learn/courses/30/lessons/59043
SELECT A.ANIMAL_ID, A.NAME FROM ANIMAL_OUTS A
LEFT JOIN ANIMAL_INS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.DATETIME < B.DATETIME ORDER BY B.DATETIME;

#카드정렬하기
#https://www.acmicpc.net/problem/1715
import heapq
import sys

n = int(sys.stdin.readline())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(sys.stdin.readline()))

answer = 0
while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    answer += a + b
    heapq.heappush(cards, a+b)
print(answer)
