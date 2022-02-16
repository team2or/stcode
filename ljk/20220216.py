n=int(input())

list=[]
cnt=0
while n!=1:
    list.append(n)
    if n%3==0:
        n=n//3
    elif n%2==0:
        if (n-1)%3==0:
            n=n-1        
        else:
            n=n//2
    else:
        n-=1
    cnt+=1
list.append(1)
print(cnt)
for i in list:
    print(i,end=' ')
