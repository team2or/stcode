#IOIOI

n = int(input())
m= int(input())
s= input()
	
n <= 100
m <= 10000
p=''
for i in range(2*n+1):
    if i %2==0:
        p+='I'
    else:
        p+='O'
cnt=0
for j in range(m-len(p)+1):
    if s[j:len(p)+j]==p:
        cnt+=1
print(cnt)
#50점
from sys import stdin
input = stdin.readline

def sol(n,m,s):
    ans = 0
    cnt = 0
    i = 1
    while i < m-1:
        if s[i-1]== 'I' and s[i]=='O' and s[i+1]=='I':
            cnt+=1
            if cnt == n:
                cnt-=1
                ans+=1
            i+=1
        else:
            cnt=0
        i+=1
    return ans
if __name__=="__main__":
    n = int(input())
    m= int(input())
    s= input()
    answer= sol(n,m,s)
    print(answer)




 
