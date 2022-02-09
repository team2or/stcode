#기타줄
n,m= map(int, input().split())
packages=[]
ones=[]
for _ in range(m):
    package, one=map(int, input().split())
    packages.append(package)
    ones.append(one)
if min(packages)> min(ones)*(n%6):
    print((n//6)*min(packages)+(n%6)*min(ones))
elif ((n//6)+1)*min(packages) > n*min(ones):
    print(n*min(ones))
else:
    print(((n//6)+1)*min(packages))


