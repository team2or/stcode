def solution(s, n):
    an=''
    for i in s:
        if i != ' ':
            plus=ord(i)+n
            if i.islower() and plus > ord('z') or \
                i.isupper() and plus > ord('Z'):
                '''대소문자별로 경우를 나누고 
                만약 아스키코드 변환시 z변환수 보다 클경우
                숫자 변환값에서 26을 빼서 a,A값부터 시작하게 함'''
                plus=plus-26
            an+=chr(plus)
        else:
            an+=i
    return an
solution('A b z', 4)



        