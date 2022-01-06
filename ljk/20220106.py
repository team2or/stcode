#지그재그게임
for i in range(int(input())):
    result=0
    for j in range(1,int(input())+1):
        if j%2==0:
            result-=j      
        else:
            result+=j  
    print(f'#{i+1} {result}')

#369게임
import re
for i in range(1,int(input())+1):
    j=str(i)
    if '3' in j or '6' in j or '9' in j:
        j=re.sub('[369]','-',j)
        j=re.sub('[^-]','',j)
        print(j, end=' ')
    else:
        print(i, end=' ')

########################################정규표현식이 적용이 안됨


for i in range(1,int(input())+1):
    j=str(i)
    if '3' in j or '6' in j or '9' in j:
        answer=''
        for k in j:
            if k=='3' or k=='6' or k=='9':
                answer+='-'
            else:
                answer+=''
        print(answer, end=' ')
    else:
        print(i, end=' ')

