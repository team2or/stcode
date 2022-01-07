#1976. 시각 덧셈
for i in range(int(input())):
    time=list(map(int, input().split()))
    hour=time[0]+time[2]
    minu=time[1]+time[3]
    if minu > 60:
        minu-=60
        hour+=1
    if hour >12:
        hour-=12
    print(f'#{i+1} {hour} {minu}')


#1936. 1대1 가위바위보

A,B= map(int,input().split())
if A>B:
    print('A')
else:
    print('B')
    