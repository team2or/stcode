#반복수열
import sys

a,p= map(int, sys.stdin.readline().split())

result=[a]
while True:
    tmp=0
    for s in str(result[-1]):
        tmp+=int(s)**p

    if tmp in result:
        break

    result.append(tmp)

print(result.index(tmp))
