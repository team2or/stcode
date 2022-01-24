# https://www.acmicpc.net/problem/11047
# BeakJoon 11047.

N, K = map(int, input().split()) 
coin = list()
for i in range(N):
    coin.append(int(input()))

total = 0
for i in reversed(range(N)):
    total += K//coin[i]
    K = K%coin[i]

print(total)