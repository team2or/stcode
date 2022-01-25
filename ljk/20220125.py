#ATM
n=int(input())
times=list(map(int, input().split()))
times.sort()
answer=0
for i in range(1,n+1):
    answer+=sum(times[:i])
print(answer)



#거스름돈
money=1000-int(input())
changes=[500,100,50,10,5,1]
answer=0
for change in changes:
    if money>=0:
        answer+=money//change
        money=money%change
print(answer)
