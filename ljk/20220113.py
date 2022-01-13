#다리 놓기
# m개 중에 n개를 골라 순서상관없는 조합 fac(m)//(fac(m-n)*fac(n))

from math import *
t=int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(comb(m,n))
############################################    
from math import factorial as fac
t=int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(fac(m)//(fac(m-n)*fac(n)))
#######################################
dp = [0] * 31
dp[0] = 1
dp[1] = 1

for i in range(2, 31):
  dp[i] = dp[i-1] * i # factorial을 리스트에 저장
 
T = int(input())
for i in range(T):
  n, m = map(int, input().split())
  a = dp[m-n]
  b = dp[m]
  c = dp[n]
  print(b//(a*c))
  print((b//a)//c)









#공 바꾸기

n, m = map(int,input().split())
order={}
for a in range(1,n+1):
    order[f'{str(a)}']=a
for _ in range(m):
    i, j = map(int, input().split())
    order[f'{str(i)}'],order[f'{str(j)}']=order[f'{str(j)}'],order[f'{str(i)}']
answer=[x for x in order.values()]
for k in answer:
    print(k, end=' ')