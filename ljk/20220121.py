#일요일
cnt=1
ms={'MON':1,'TUE':2,'WED':3,'THU':4,'FRI':5,'SAT':6,'SUN':7}
for _ in range(int(input())):  
    answer=7-ms[input()]
    if answer==0:
        print(f'#{cnt} 7')
        cnt+=1
    else:
        print(f'#{cnt} {answer}')
        cnt+=1

#튜플
def solution(a):
    a=a.replace('{','')
    a=a.replace(',',' ')
    a=a.split('}')
    li=[]
    for i in a:
        i=i.split()
        basket=[]
        for j in i:
            if j.isdigit():
                basket.append(int(j))
        if len(basket)>0:
            li.append(basket)
    li=sorted(li, key=lambda x: len(x))
    answer=[]
    for i in li:
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer

solution("{{20,111},{111}}")
a="{{20,111},{111}}"
a=a.replace('{','')
a=a.replace(',',' ')
a=a.split('}')
li=[]
for i in a:
    i=i.split()
    basket=[]
    for j in i:
        if j.isdigit():
            basket.append(int(j))
    if len(basket)>0:
        li.append(basket)
li=sorted(li, key=lambda x: len(x))
answer=[]
for i in li:
    for j in i:
        if j not in answer:
            answer.append(j)
answer
import re
from collections import Counter
s="{{20,111},{111}}"
s = Counter(re.findall('\d+', s))
s
s.rstrip('}').lstrip('{')
s1 = s.lstrip('{').rstrip('}').split('},{')
s1
(re.findall('\d+', s))