import sys

n = int(sys.stdin.readline())

work = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
work.sort()

dp = [0]*1000
for d, w in work:
    if dp[d-1] ==0:
        dp[d-1] = w
    else:
        min_value = 100
        for i in range(d):
            if min_value > dp[i]:
                min_value = dp[i]
                idx = i
        dp[idx] = w
print(sum(dp))