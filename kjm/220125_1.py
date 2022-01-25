# https://www.acmicpc.net/problem/11399
# BaekJoon 11399.

N = int(input())
T = list(map(int, input().split(" ")))
T.sort()
t = 0
result = []
for i in T:
    t += i
    result.append(t)

print(sum(result))