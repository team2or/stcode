#1만들기

n=int(input())
dp=[0]*(n+1)
dp[0]=-1
for i in range(1,n+1):
    if dp[i]==0:
        dp[i]=dp[i-1]+1
        if i%3==0:
            if dp[i]>dp[i//3]+1:
                dp[i]=dp[i//3]+1
        if i%2==0:
            if dp[i]>dp[i//2]+1:
                dp[i]= dp[i//2]+1
print(dp[n])



#1만들기 2

n=int(input())
dp=[[0,0]]*(n+1)
dp[0]=[-1,-1]
for i in range(1,n+1):
    dp[i]=[dp[i-1][0]+1, i-1]
    if i%2==0:
        if dp[i][0]>dp[i//2][0]+1:
            dp[i]=[dp[i//2][0]+1, i//2]
    if i%3==0: 
        if dp[i][0] > dp[i//3][0]+1:
            dp[i]=[dp[i//3][0]+1, i//3]
print(dp[n][0])
min_, go_one= dp[n]
print(n,end=' ')
while go_one!=0:
    print(go_one, end=' ')
    min_, go_one=dp[go_one]
