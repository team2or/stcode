#프로그래머스_SQL
#복습1
#중복제거하기
#https://programmers.co.kr/learn/courses/30/lessons/59408
#DISTINCT로 중복제거 WHERE절로 NULL인 이름 제거 후 count로 이름개수 세기
SELECT count(DISTINCT NAME) FROM ANIMAL_INS WHERE NAME IS NOT NULL;

#복습2
#보호소에서 중성화한 동물
#https://programmers.co.kr/learn/courses/30/lessons/59045
#이전답안
SELECT OUTS.ANIMAL_ID, OUTS.ANIMAL_TYPE, OUTS.NAME FROM ANIMAL_INS INS LEFT JOIN ANIMAL_OUTS OUTS ON INS.ANIMAL_ID = OUTS.ANIMAL_ID WHERE INS.SEX_UPON_INTAKE LIKE "Intact%" AND OUTS.SEX_UPON_OUTCOME NOT LIKE "Intact%";

#이번답안
SELECT OUTS.ANIMAL_ID, OUTS.ANIMAL_TYPE, OUTS.NAME FROM (SELECT * FROM ANIMAL_INS INS WHERE INS.SEX_UPON_INTAKE LIKE "Intact%") INS LEFT JOIN ANIMAL_OUTS OUTS ON INS.ANIMAL_ID=OUTS.ANIMAL_ID WHERE OUTS.SEX_UPON_OUTCOME NOT LIKE "Intact%" ORDER BY OUTS.ANIMAL_ID;

#다른답안
#출처:https://mungto.tistory.com/282
#들어온 상태와 나갔을 때의 상태가 다르면 중성화가 된거기 때문에
SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME 
FROM ANIMAL_INS as I JOIN ANIMAL_OUTS as O 
WHERE I.ANIMAL_ID = O.ANIMAL_ID AND I.SEX_UPON_INTAKE != O.SEX_UPON_OUTCOME
ORDER BY I.ANIMAL_ID


#프로그래머스
#복습/힙
#더맵게
#https://programmers.co.kr/learn/courses/30/lessons/42626
#이전답안
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) > 1:
            n = heapq.heappop(scoville)
            s = heapq.heappop(scoville)
            if K > n:
                heapq.heappush(scoville, n + (s*2))
                answer += 1
        else:
            return -1
    return answer



#이번답안
scoville = [1, 2, 3, 9, 10, 12]
K = 7
import heapq
heapq.heapify(scoville)
answer = 0
while scoville[0] < K:
    if len(scoville) > 1:
        f = heapq.heappop(scoville)
        s = heapq.heappop(scoville)
        heapq.heappush(scoville, f+(s*2))
        answer += 1
    else:
        print(-1)
print(answer)









