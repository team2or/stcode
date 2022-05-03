#프로그래머스
#복습
#있었는데 없었습니다
#https://programmers.co.kr/learn/courses/30/lessons/59043
SELECT OUTS.ANIMAL_ID, OUTS.NAME FROM ANIMAL_INS INS LEFT JOIN ANIMAL_OUTS OUTS ON INS.ANIMAL_ID=OUTS.ANIMAL_ID WHERE INS.DATETIME > OUTS.DATETIME ORDER BY INS.DATETIME;

#완전탐색/조합
#피로도
#https://programmers.co.kr/learn/courses/30/lessons/87946
#답안:https://tiktaek.tistory.com/82
from itertools import permutations
def solution(k, dungeons):
    answer = 0
    #던전 탐험할 수 있는 모든 경우의 조합 생성
    list_dungeons = list(permutations(dungeons, len(dungeons)))
    #모든 경우의 조합을 하나씩 돌면서 주어진 피로도 내에서
    #가장많이 던전을 방문할 수 있는 수 찾기
    for dungeons in list_dungeons:
        now_k, cnt = k, 0
        for dun in dungeons:
            if dun[0] <= now_k:
                now_k -= dun[1]
                cnt += 1
            else:
                break
        answer = max(answer, cnt)
    return answer
    
#[참고]
#https://homzzang.com/b/py-133
#max(a,b)
#a,b를 비교하여 max인 값 반환

