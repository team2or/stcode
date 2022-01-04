#중간값 찾기
n=int(input())
if n<9:
    n=9
elif n>199:
    n=199
num=list(map(int,input().split()))
set_=[]
ran=int(len(num))
for i in range(ran):
    set_.append(min(num))
    num.remove(min(num))   
print(set_[(len(set_)//2)])

#서랍의 비밀번호

p,k=map(int,input().split())
cnt=1
while k!=p:
    k+=1
    cnt+=1
print(cnt)