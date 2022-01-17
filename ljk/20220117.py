#수박수박수박
def solution(n):
    answer = ''
    su='수'
    bak='박'
    for i in range(n):
        if i%2==0:
            answer+=su
        else:
            answer+=bak
    return answer

def solution(n):
    return "수박"*(n//2) + "수"*(n%2)

def solution(n):
    return ("수박"*n)[0:n]


#키패드 누르기

