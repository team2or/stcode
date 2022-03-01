#위장
def solution(clothes):
    answer = 1
    clo={}
    for cloth, types in clothes:
        value = clo.get(types)
        if value==None:
            clo[types] = [cloth]
        else:
            clo[types].append(cloth)
    for i in clo.keys():
        answer*=len(clo[i])+1
    return answer-1

solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])
