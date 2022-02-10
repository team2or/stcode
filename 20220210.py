def solution(sco, k):
    answer=0
    while k>= sorted(sco)[0]:
        sco.sort()
        sco[1]=sco[0]+sco[1]*2
        sco.remove(sco[0])
        answer+=1
        if len(sco)==1:
            if sco[0]>=k:
                return answer
            else:
                return -1
    return answer

#효율성 떨어짐

import heapq

def solution(scoville, K):
    answer = 0
    scoville.sort()
    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1
        else:
            small = heapq.heappop(scoville)
            small2 = heapq.heappop(scoville)
            heapq.heappush(scoville, (small + (small2 * 2)))
            answer += 1
    return answer

    #힙뭐시기로 쉽게