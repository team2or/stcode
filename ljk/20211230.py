def solution(n):
    for i in range(1,n):
        if n%i==1:
            return i

solution(10)

#문자열 다루기 기본

def solution(s):
    
    answer=[]
    if len(s)<4 or len(s)>6 or len(s)==5:
        return False
    elif 4<=len(s) and len(s)<=6:
        if s.isdigit()==True:
            return True
        else:
            return False