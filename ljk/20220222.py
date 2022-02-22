#이장님 초대
n= int(input())
trees=list(map(int, input().split()))
trees.sort(reverse=True)
day=1
set_date=0
for tree in trees:
    if set_date<tree:
        set_date=tree
    day+=1
    set_date-=1

print(day+set_date+1)

