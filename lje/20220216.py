# 프로그래머스_SQL
#NULL처리하기
#https://programmers.co.kr/learn/courses/30/lessons/59410
SELECT ANIMAL_TYPE, IFNULL(NAME, "No name"), SEX_UPON_INTAKE FROM ANIMAL_INS;

#루시와 엘라찾기
#https://programmers.co.kr/learn/courses/30/lessons/59046
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE FROM ANIMAL_INS WHERE NAME IN ("Lucy", "Ella", "Pickle", "Rogan", "Sabrina", "Mitty") ORDER BY ANIMAL_ID;

#동적계획법
#1로 만들기2
#https://www.acmicpc.net/problem/12852
n = int(input())
answer = 0
answer2 = ''
while n != 1:
    answer2 = answer2 + str(n) + " "
    if n%2==0:
        n -= 1
        answer += 1
    elif n%3==0:
        n //= 3
        answer += 1
answer2 += '1'
print(answer)
print(answer2)
DP = [[0,[]] for _ in range(3+1)]
DP[1][0] = 0
DP[1][1] = [1]
print(DP)

from collections import deque
n = int(input())
q = deque()
q.append([n])
answer = []

while q:
    arr = q.popleft()
    x = arr[0]
    if x == 1:
        answer = arr
        break
    if x%3 == 0:
        q.append([x//3] + arr)
    if x%2 == 0:
        q.append([x//2] + arr)
    q.append([x-1] + arr)

print(len(answer)-1)
for i in range(len(answer)-1, -1, -1):
    print(answer[i], end = " ")

print(10%2)
