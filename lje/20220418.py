#해커랭크
#복습
#Ollivander's Inventory
#https://www.hackerrank.com/challenges/harry-potter-and-wands/problem?isFullScreen=true
from dis import dis
from tkinter import N


SELECT W.id, WP.age, W.coins_needed, W.power FROM Wands W LEFT JOIN Wands_Property WP
ON W.code = WP.code WHERE W.coins_needed = (SELECT min(W1.coins_needed) FROM Wands W1 LEFT JOIN Wands_Property WP1 ON W1.code = WP1.code WHERE WP.is_evil = 0 AND W.power = W1.power AND WP.age = WP1.age) ORDER BY W.power DESC, WP.age DESC;

#프로그래머스
#다익스트라/다이나믹 프로그래밍
#배달
#https://programmers.co.kr/learn/courses/30/lessons/12978
import heapq
def solution(N, road, K):
    dist = [float('inf')]*(N+1)
    dist[1] = 0
    roads = [[] for _ in range(N+1)]
    for r in road:
        roads[r[0]].append([r[2], r[1]])
        roads[r[1]].append([r[2], r[0]])
    print(roads)
    heap = []
    heapq.heappush(heap, [0,1])
    while heap:
        print(heap)
        cost, node = heapq.heappop(heap)
        for c, n in roads[node]:
            print(f"cost:{cost} node:{node}")
            print(f"cost:{c} node:{n}")
            if cost+c < dist[n]:
                dist[n] = cost+c
                heapq.heappush(heap, [cost+c, n])
        print(dist)
    return len([i for i in dist if i <= K])

solution(5,	[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)
#[참고]
#https://jennnn.tistory.com/83