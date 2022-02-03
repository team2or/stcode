#비밀지도
def solution(n, arr1,arr2):
    arr_1=[]
    arr_2=[]
    answer=[]
    for i in arr1:
        arr_1.append(format(i,'b').zfill(n))
    for j in arr2:
        arr_2.append(format(j,'b').zfill(n))
    for k in range(n):
        ans=''
        for l in range(n):
            if arr_1[k][l]=='1'or arr_2[k][l]=='1':
                ans+='#'
            else:
                ans+=' '
        answer.append(ans)
    return answer
solution(5, [9, 20, 28, 18, 11],[30, 1, 21, 17, 28])

def solution(n, arr1, arr2):
    answer=[]
    for i, j in zip(arr1,arr2):
        a12=bin(i|j)[2:].zfill(n) #bin함수로 2진수 겹치는 부분 자동 적용
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer