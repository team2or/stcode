#보석 도둑
import heapq
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
jw=[]
for _ in range(n):
    m, v= map(int, input().split())
    heapq.heappush(jw, [m,v])
bags=[]
for _ in range(k):
    c= int(input())
    heapq.heappush(bags, c)

answer=0
capable=[]

for _ in range(k):
    bag= heapq.heappop(bags)

    while jw and bag >=jw[0][0]:
        [m, v] = heapq.heappop(jw)
        heapq.heappush(capable, -v)

    print(capable)
    if capable:
        answer-= heapq.heappop(capable)
    elif not jw:
        break

print(answer)

#heapq.heappush 를 하면 첫 인덱스 값은 최소 값이 맞다.
#하지만 그 뒤는 최소값 다음 값인지는 모른다.
#그래서 -를 입혀 최댓값을 구하는 것이다.
#양수값으로 할 경우 최댓값이 먼저 들어왔을 경우 최소값이 아닌 경우에 최댓값 뒤로 갈수 도 있어
#pop은 옳바른 방법이 아니다.