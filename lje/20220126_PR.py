#프로그래머스
#최소직사각형
#https://programmers.co.kr/learn/courses/30/lessons/86491
def solution(sizes):
    w = []
    h = []
    for i in sizes:
        if i[0] >= i[1]:
            w.append(i[0])
            h.append(i[1])
        else:
            w.append(i[1])
            h.append(i[0])
    return max(w)*max(h)

#다른 답안
def solution(sizes):
    #for문으로 두수 중 큰 값, 작은 값 리스트 만들어 그 리스트 중 큰 값을 서로 곱함
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

#예산
#https://programmers.co.kr/learn/courses/30/lessons/12982
def solution(d, budget):
    answer = 0
    if sum(d) <= budget:
        answer = len(d)
    else:
        count = 0
        for i in sorted(d):
            if count <= budget:
                count += i
                if count <= budget:
                    answer += 1
    return answer
solution([1,3,2,5,4],9)
solution([2,2,3,3],10)

#다른 답안
def solution(d, budget):
    d.sort()
    #신청금액의 합이 예산보다 많을 때
    #맨 마지막 값 제거/ del로 제거해도 될듯
    while budget < sum(d):
        d.pop()
    return len(d)