#주유소
n= int(input())
roads=list(map(int, input().split()))
citys=list(map(int, input().split()))
answer=0
if citys[0]==min(citys):
    answer+=citys[0]*sum(roads)

elif citys[0]!= min(citys):
    answer+=citys[0]*roads[0]

print(answer)