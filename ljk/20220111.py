#문자열을 정수로 바꾸기

def solution(s):
    return int(s)

#체육복

def solution(n,lost,reserve):
    lost.sort()
    for i in lost[:]:
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)
    for j in lost[:]:
        if j-1 in reserve:
            lost.remove(j)
        elif j+1 in reserve:
            lost.remove(j)
    return n-len(lost)





def solution(n,lost,reserve):
    okay=[]
    for i in reserve:
        if i in lost:
            okay.append(i)
    reserve=list(set(reserve)-set(okay))
    lost=list(set(lost)-set(okay))
    
    for j in  reserve:
        if j-1 in lost:
            lost.remove(j-1)
        elif j+1 in lost:
            lost.remove(j+1)
    return n-len(lost)