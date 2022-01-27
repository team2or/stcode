#약수의 개수와 덧셈
def solution(x,y):
    sum=0
    for i in range(x,y+1):
        a=[]
        for j in range(1,i+1):
            if i%j==0:
                a.append(j)
        if len(a)%2==0:
            sum+=i
        else:
            sum-=i
    return sum

#다트게임
def solution(dartResult):
    list=[]
    dartResult=dartResult.replace('10','A')
    for i in dartResult:
        if i.isdigit():
            list.append(int(i))
        elif i=='A':
            list.append(int(10))
        elif i=='S':
            list[-1]**=1
        elif i=='D':
            list[-1]**=2
        elif i=='T':
            list[-1]**=3
        elif i=='*':
            if len(list)>1:
                list[-2]*=2
            list[-1]*=2
        elif i=='#':
            list[-1]*=-1
    return sum(list)

import re
re.compile()
dartresult='1D#2S*3S'
p = re.compile('(\d+)([SDT])([*#]?)')
p.findall(dartresult)