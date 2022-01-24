#동전0
n,k=map(int,input().split())
use_coin=[]
answer=0
for i in range(n):
    use_coin.append(int(input()))
for j in use_coin[::-1]:
    while k-j>=0:
        k-=j
        answer+=1
print(answer)

###시간초과-> 값을 바로 계산
n,k=map(int,input().split())
use_coin=[]
answer=0
for i in range(n):
    use_coin.append(int(input()))
for j in use_coin[::-1]:
    answer+=k//j
    k=k%j
print(answer)

#대회 or인턴

n,m,k= map(int,input().split())
cnt=0
while n+m-k>=3 and n>=2 and m>=1:
    n-=2
    m-=1
    cnt+=1
print(cnt) 