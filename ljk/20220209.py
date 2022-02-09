#기타줄
n,m= map(int, input().split())
packages=[]
ones=[]
for _ in range(m):
    package, one=map(int, input().split())
    packages.append(package)
    ones.append(one)
pack_min=min(packages)
one_min=min(ones)
print(min([pack_min*(n//6+1), pack_min*(n//6)+one_min*(n%6), one_min*n, ]))



