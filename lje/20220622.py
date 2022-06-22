#프로그래머스_SQL
#어린 동물 찾기
#https://programmers.co.kr/learn/courses/30/lessons/59037
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE NOT INTAKE_CONDITION = 'Aged';

#프로그래머스
#로또의 최고순위와 최저순위
#https://programmers.co.kr/learn/courses/30/lessons/77484
lottos = [44,1,0,0,31,25]
win_nums = [31,10,45,1,6,19]
lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]
lottos = [1,2,3,4,5,6]
win_nums = [7,8,9,10,11,12]
rank = 7
answer = []
for i in range(6):
    if lottos[i] in win_nums:
        rank -= 1
if rank == 7:
    if lottos.count(0) == 0:
        answer.append([rank-1, rank-1])
    else:
        answer.append([rank-lottos.count(0), rank-1])
else:
    answer.append([rank-lottos.count(0), rank])
print(answer)

#다른답안
#집합을 이용한 풀이
def solution(lottos, win_nums):
    #rank를 사전형으로 만듦
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    #set으로 list변경 후 교집합되는 수 찾으면 최소순위를 알 수 있음
    #최고순위는 lottos에 0의 숫자를 count해서 더해주면 됨
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]

#다른답안
#여기서도 순위를 먼저 list로 생성
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]