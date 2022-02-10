# 프로그래머스_SQL
# 동물수구하기
# https://programmers.co.kr/learn/courses/30/lessons/59406
import heapq
SELECT COUNT(ANIMAL_ID) as count FROM ANIMAL_INS

# 중복제거하기
# https://programmers.co.kr/learn/courses/30/lessons/59408
# 중복제거 코드 DISTINCT
# COUNT를 사용하면 NULL인 것은 카운트하지 않음
# https://bae9086.tistory.com/154
SELECT COUNT(DISTINCT NAME) as count FROM ANIMAL_INS

# 더맵게
# https://programmers.co.kr/learn/courses/30/lessons/42626

# 최종답


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


solution([1, 2, 3, 9, 10, 12], 7)


# heapq 모듈 사용하여 풀어야 함
# https://korshika.tistory.com/5
# sort로 풀려고 하면 런타임 오류 뜸
def solution(scoville, K):
    answer = 0
    while scoville[0] < K:
        for i in range(0, 1):
            print(scoville)
            if K > scoville[i]:
                scoville[i+1] = scoville[i] + (scoville[i+1] * 2)
                del scoville[i]
                scoville.sort()
                answer += 1
    return answer


solution([1, 2, 3, 9, 10, 12], 7)
