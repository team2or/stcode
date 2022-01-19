#문자열 내림차순으로 배치하기
def solution(s):
    upper=[]
    low=[]
    for i in s:
        if i.isupper():
            upper.append(i)
        else:
            low.append(i)
    low.sort()
    low.reverse()
    upper.sort()
    upper.reverse()
    return ''.join(low)+''.join(upper)



