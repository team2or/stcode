px = [5,1,3,2]
result = 0
mx = max(px)
for i in range(1,len(px)):
    num = px[:i]
    mi = min(num)
    m = max(num)
    if result < px[i]-mi:
        print(px[i], mi)
        result = px[i]-mi
    if px[i] == mx:
        break
if result == 0:
    print(-1)
else:
    print(result)

def maxDifference(px):
    # Write your code here
    pass_num = []
    result = 0
    m = max(px)
    for p in px:
        if len(pass_num) > 0:
            pass_num.append(p)
            num = pass_num[:pass_num.index(p)]
            for n in num:
                if p > n:
                    max_num = abs(p-n)
                    if result < max_num:
                        result = max_num
        else:
            pass_num.append(p)
    if result == 0:
        return -1
    else:
        return result
maxDifference([6,7,9,5,6,3,2])


n = 10
start = [3,8]
finish = [4,9]
visited = [0]*n
for i, j in zip(start, finish):
    for v in range(i-1,j):
        visited[v] = 1

count = 0
dist = []
for visit in visited:
    if visit == 0:
        count += 1
    else:
        dist.append(count)
        count = 0
print(max(dist))


n = 10
start = [3,8]
finish = [4,9]
st = 1
count = (start[0]-st)
for s in range(1,len(start)):
    for f in range(len(finish)):
        if count < (start[s]-1)-finish[f]:
            count = (start[s]-1)-finish[f]
print(count)