#주유소
n= int(input())
roads=list(map(int, input().split()))
citys=list(map(int, input().split()))
answer=0
if citys[0]==min(citys):
    answer+=citys[0]*sum(roads)

else:
    answer=roads[0]*citys[0]
    min_city=citys[0]

    for i in range(1,n-1):
        if min_city> citys[i]:
            min_city=citys[i]
        answer+=min_city*roads[i]

print(answer)