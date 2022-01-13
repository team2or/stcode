# https://www.acmicpc.net/problem/10813
# BeakJoon 10813.

n,m=map(int,input().split())
a=[i for i in range(n+1)]
for j in range(m):
  i,j=map(int,input().split())
  a[i],a[j]=a[j],a[i]

for k in a[1:]:
    print(k, end = " ")