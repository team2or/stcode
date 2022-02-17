#바이러스

n=int(input())
m=int(input())

connect=[]
for _ in range(m):
    a,b= map(int, input().split())
    connect.append([a,b])
cnt=0
list=[1]
while cnt!=50:
    for i in connect:
        for j in list:
            if j in i:
                for k in i:
                    list.append(k)
    cnt+=1
print(len({list}))


