# 프로그래머스_SQL
#이름에 el이 들어가는 동물 찾기
#https://programmers.co.kr/learn/courses/30/lessons/59047
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE NAME LIKE "%EL%" AND ANIMAL_TYPE = "Dog" ORDER BY NAME;

#중성화 여부 파악하기
#https://programmers.co.kr/learn/courses/30/lessons/59409
SELECT  ANIMAL_ID, NAME,
CASE SEX_UPON_INTAKE WHEN "Neutered Male" THEN 'O' WHEN "Spayed Female" THEN 'O' ELSE 'X' END AS "중성화" FROM ANIMAL_INS ORDER BY ANIMAL_ID;

#다른 답안
#출처: https://mentha2.tistory.com/102 [행궁동 데이터 엔지니어]
#WHEN절을 OR로 묶어서 한번에 처리할 수 있음
#LIKE로 처리했었는데 오답이라해서 안썼는데 다른 곳에서 오류였던 듯 싶다.
SELECT ANIMAL_ID, NAME, CASE WHEN (SEX_UPON_INTAKE LIKE '%NEUTERED%' OR SEX_UPON_INTAKE LIKE '%SPAYED%') THEN 'O' ELSE 'X' END AS '중성화' FROM ANIMAL_INS ORDER BY ANIMAL_ID ASC

#그래프 탐색
#바이러스
#https://www.acmicpc.net/problem/2606
count = int(input())
arr_num = int(input())
arr = []
answer = []
for _ in range(arr_num):
    arr.append(list(map(int, input().split())))

for i in arr:
    if 1 in i:
        answer.append(i.pop())
    if answer[-1] in i:
        n = i.pop()
        if n not in answer:
            answer.append(n)
print(len(answer))
print(arr)

#답안 참고 수정
#https://soojong.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-2606-%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4

count = int(input())
arr_num = int(input())
arr = [list(map(int, input().split())) for _ in range(arr_num)]

que = [1] #첫시작은 1번 컴퓨터
answer = [] #감염된 컴퓨터들

#연결된 컴퓨터들(que)이 없을 때까지 반복
while len(que) != 0:
    vir = que.pop(0)
    for i in arr:
        if vir in i:
            i.remove(vir)
            v = i.pop()
            if v not in answer:
                que.append(v)
                answer.append(v)
print(len(answer))