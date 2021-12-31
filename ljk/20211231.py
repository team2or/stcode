#더하기사이클
#시간초과
n_=input()
cnt=0
n=n_
while True:
    if len(n)==1:
        n+='0'
    a=int(n[0])+int(n[1])
    if len(str(a))==2:
        inte=(n[1]+str(a)[1])
    else:
        inte=(n[1]+str(a)[0])
    cnt+=1
    n=inte
    if inte==n_:
        print(cnt)
        break
#숫자로
n_=int(input())
cnt=0
n=n_
while True:
    a= n//10
    b= n%10
    c= (a+b)%10
    n=b*10+c
    cnt+=1
    if n==n_:
        print(cnt)
        break

#숫자의 합
n=int(input())
num=input()
inte=0
for i in num:
    inte+=int(i)
print(inte)