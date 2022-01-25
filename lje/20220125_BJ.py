#백준
#거스름돈 - 동전0 복습용
#https://www.acmicpc.net/problem/5585
m = int(input())
coins = [500,100,50,10,5,1]
count = 0
change = 1000-m
for i in coins:
    count += change//i
    change = change%i

print(count)

#ATM
#https://www.acmicpc.net/problem/11399
p = int(input())
time = sorted(list(map(int, input().split())))
answer = 0
for i in range(len(time)+1):
    answer += sum(time[:i])

print(answer)