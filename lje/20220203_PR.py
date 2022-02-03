import re
def solution(n, arr1, arr2):
    answer = []
    fs = []
    ss = []
    for i in range(n):
        f = re.sub(r'[^0-9]', '', bin(arr1[i]))
        s = re.sub(r'[^0-9]', '', bin(arr2[i]))
        if len(f) < n:
            f = "0"*(n-len(f)) + f
        if len(s) < n:
            s = "0"*(n-len(s)) + s
        fs.append(f[-n:])
        ss.append(s[-n:])
    for i in range(n):
        w = ''
        for j in range(n):
            if fs[i][j] == '1' or ss[i][j] == '1':
                w += '#'
            else:
                w += ' '
        answer.append(w)
    return answer

solution(5, [9, 20, 28, 18, 11],[30, 1, 21, 17, 28])
solution(6, [46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10])

#다른답안
def solution(n, arr1, arr2):
    answer = []
    #zip으로 arr1과 arr2를 묶어 for문 사용
    for i,j in zip(arr1,arr2):
        #비트연산자 |(or)을 사용
        #https://wikidocs.net/1161
        a12 = str(bin(i|j)[2:])
        print(bin(i|j))
        #n만큼 문자 길이 맞추기
        #https://kkamikoon.tistory.com/entry/Python-%EC%8A%A4%ED%8A%B8%EB%A7%81-%EC%95%9E%EC%97%90-0-%EC%B1%84%EC%9A%B0%EB%8A%94-%EB%B0%A9%EB%B2%95zfill-rjust
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer