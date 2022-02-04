#30
import math
import itertools
N=input()
list_=[]
integers=[]
for i in N:
    list_.append(i)
list_=list(itertools.permutations(list_,len(N)))
n=math.factorial(len(N))
for i in range(n):
    integers.append(int(''.join(list(list_[i]))))
answer=0
for j in integers:
    if j%30==0 and j>answer:
        answer=j
if answer==0:
    print(-1)
else:
    print(answer)

#메모리 초과 itertools.permutation
import itertools
integers=[]
n=input()
list_=list(itertools.permutations(n,len(n)))
for i in range(len(list_)):
    integers.append(int(''.join(list(list_[i]))))
answer=0
for j in integers:
    if j%30==0 and j>answer:
        answer=j
if answer==0:
    print(-1)
else:
    print(answer)

n=input()
n=sorted(n, reverse=True)
if '0' not in n:
    print(-1)
else:
    sum=0
    for i in n:
        sum+=int(i)
    if sum%3 !=0:
        print(-1)
    else:
        print(''.join(n))