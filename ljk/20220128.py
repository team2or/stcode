#로프
lo=[]
answer=0
for _ in range(int(input())):
    lo.append(int(input()))
lo.sort()
for i in lo:
    print(i)
    weight=i*len(lo)
    lo.remove(i)
    print(lo)
    if answer<weight:
        answer=weight
print(answer)

a=[1,2,1,3]
a.remove(1)
a