#프로그래머스
#두 정수 사이의 합
#https://programmers.co.kr/learn/courses/30/lessons/12912

def solution(a,b):
    answer = 0
    if a <= b:
        for i in range(a,b+1):
            answer += i
    else:
        for i in range(b,a+1):
            answer += i 
    return answer

solution(3,5)
solution(3,3)
solution(5,3)

#신규 아이디 추천
#https://programmers.co.kr/learn/courses/30/lessons/72410
import re
def solution(new_id):
    #1단계/2단계 대문자->소문자 변경,알파벳소문자,숫자,'-,_,.'제외 제거
    new_id = re.sub('[^a-z\d\-\_\.]', '', new_id.lower())
    #3단계 여러개의 '.' 하나로 변경
    new_id = re.sub('\.+', '.', new_id)
    #4단계 첫번째 시작이 마침표라면 제거
    if new_id[0] == '.':
        new_id= re.sub(r'^.','', new_id)
    #4단계 마지막이 마침표라면 제거
    if new_id[-1] == '.':
        new_id= re.sub(r'.$','', new_id)
    #5단계 빈문자열이라면 'a'대입
    if len(new_id) == 0:
        new_id = 'a'
    #6단계 길이 16자 이상이면 15자 이후 글자 삭제
    #      제거 후 마침표로 끝나면 마침표 제거
    elif len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id= re.sub(r'.$','', new_id)
    #7단계 new_id길이가 2자 이하면 마지막 문자 반복하여 길이 3으로 맞춤.
    if len(new_id) < 3:
        while len(new_id) < 3:
            new_id += new_id[-1]
    return new_id

solution("...!@BaT#*..y.abcd_efghijklm.")
solution("z-+.^.")
solution("=.=")
solution("123_.def")
solution("abcdefghijklmn.p")
solution("...!@BaT#*..y.abcd_efghijklㄴㅇㄻm.")
solution("bc")
solution('')

#제출답
import re
def solution(new_id):
    #1단계 대문자->소문자 변경
    new_id = new_id.lower()
    #2단계 특수문자 제거
    new_id = re.sub('[~!@#$%^&*\(\)=+\[\{\]\}:?,\<\>/]', '', new_id)
    #3단계 여러개의 '.' 하나로 변경
    new_id = re.sub('\.+', '.', new_id)
    #4단계 시작과 끝이 마침표라면 제거
    new_id = new_id.strip('.') #정규식 두번써서 제거하니 런타임오류(2,22,23) 뜸.
    #5단계 빈문자열이라면 'a'대입
    if new_id == '':
        new_id = 'a'
    #6단계 길이 16자 이상이면 15자 이후 글자 삭제
    #      제거 후 마침표로 끝나면 마침표 제거
    if len(new_id) > 15 :
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id= re.sub(r'.$','', new_id)
    #7단계 new_id길이가 2자 이하면 마지막 문자 반복하여 길이 3으로 맞춤.
    if len(new_id) < 3:
        while len(new_id) < 3:
            new_id += new_id[-1]
    return new_id