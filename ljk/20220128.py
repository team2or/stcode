#로프
lo=[]
answer=0
for _ in range(int(input())):
    lo.append(int(input()))
lo.sort()
for i in lo:
    weight=lo[0]*len(lo)
    lo.remove(lo[0])
    if answer<weight:
        answer=weight
print(answer)


N=int(input())
lo=[]
answer=[]
for _ in range(N):
    lo.append(int(input()))
lo.sort(reverse=True)
for i in range(N):
    answer.append((i+1)*lo[i])
print(max(answer))

#회의실 배정
time=[]
n=int(input())
for _ in range(n):
    start,end=map(int, input().split())
    time.append((start,end))
time.sort()
answer=0
e_point=time[0][1]
for i in range(n-1):
   print(time[i+1][0])
   if e_point<=time[i+1][0]:
       e_point=time[i+1][1]
       answer+=1
print(answer)


time=[]
n=int(input())
for _ in range(n):
    start,end=map(int, input().split())
    time.append((start,end))
time.sort(key=lambda x:(x[1],x[0]))
cnt=1
e_time=time[0][1]
for i in range(1,n):
    if time[i][0]>= e_time:
        cnt+=1
        e_time=time[i][1]
print(cnt)