#정수 제곱근 판별

def solution(n):
    for i in range(1,n+1):
        if n/i==i:
            return (i+1)**2
        else:
            pass
    return -1

def solution2(n):
    t=int(n**(1/2)) #제곱근은 1/2을 제곱해주면 된다.
    if t**2==n:
        return (t+1)**2
    else:
        return -1
    
#이상한 문자 만들기

def letter(s):
    answer = ''
    split_=s.split(' ')
    print(split_)
    for i in split_:
              
        for j in range(len(i)):
            if i=='':
                answer+= ' '
            elif j%2==0:
                answer+=i[j].upper()
            else:
                answer+=i[j].lower()
        if i== split_[len(split_)-1]:
            pass
        else:
            answer+=' '
    return answer
letter('ddd hello dddd    piec  ')
# 공백이 중간에 여러개인 경우에 에러가 난다고 함.

def letter2(s):
    answer = []
    words = s.split(" ")
    print(words)
    for word in words:
        w = ""
        for i in range(len(word)):
            if i % 2:
                w += word[i].lower()
            else:
                w += word[i].upper()
        answer.append(w)
        print(answer)
    return ' '.join(answer)
        


letter2("try hello  world    ")

