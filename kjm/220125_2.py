# https://www.acmicpc.net/problem/5585
# BaekJoon 5585.

coin = [500, 100, 50, 10, 5, 1]
change = 1000 - int(input())
cnt = 0
for i in coin:
    cnt += change//i
    change = change%i
    
print(cnt)