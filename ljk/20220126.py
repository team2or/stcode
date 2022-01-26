#최소직사각형 
def solution(sizes):
    ma=[]
    mi=[]
    for i in sizes:
        ma.append(max(i))
        mi.append(min(i))
    return max(ma)*max(mi)

solution([[60, 50], [30, 70], [60, 30], [80, 40]])

#예산
def solution(d, budget):
    cnt=0
    d.sort()
    for i in d:
        if budget-i>=0:
            budget=budget-i
            cnt+=1
    return cnt

solution([1,3,2,5,4],9)
        