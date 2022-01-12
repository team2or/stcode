# 두 정수 사이의 합
def solution(a,b):
    answer=0
    if a>b:
        a,b=b,a
    for i in range(a,b+1):  #sum(range(a,b+1))
        answer+=i
    return answer


#신규 아이디 추천

def solution(new_id):
    import re
    new_id=new_id.lower()
    new_id=re.sub('[^a-z0-9-_. ]','',new_id) #알파벳소문자, 숫자, -, _, . 외 제거
    new_id=new_id.replace(' ','a') # 빈칸 a로 치환
    while '..' in new_id:               #.. 이 있을경우 없을 때까지 .로 치환
        new_id=new_id.replace('..','.')
    if new_id[0]=='.':              #맨 앞이 .일 경우 제거
        new_id=new_id[1:]
    if new_id=='':                  #.제거 후 에 빈칸일 경우 a로 치환
        new_id=' '
        new_id=new_id.replace(' ','a')
    if new_id[-1]=='.':             #맨 뒤도 마찬가지로 .제거
        new_id=new_id[:-1]
    if len(new_id)>15:              #길이 15로 맞춤
        new_id=new_id[:15]
        if new_id[-1]=='.':            #길이 15로 맞춘 후 맨 뒤가 .일 경우 . 제거
            new_id=new_id[:-1]
    elif len(new_id)<3:             #길이가 3이 안 될 경우 맨 뒤 문자 길이 3일 때까지 삽입
        while len(new_id)<3:
            new_id+=new_id[-1]
    return new_id


re.sub('^[.]|[.]$', '', a) #앞뒤 바꿔주기 ^ 시작 /% 끝  '|' 또는
'a' if len(st) == 0 else st[:15] #-깔끔-


def solution(str):
    import re
    str=str.lower()
    str=re.sub('[^a-z0-9\-_.]','', str)
    while '..' in str:
        str=str.replace('..','.')
    str=re.sub('^[.]|[.]$','',str)
    str= 'a' if str=='' else str[:15]
    str=re.sub('^[.]|[.]$','',str)
    if len(str)<3:
        while len(str)<3:
            str+=str[-1]
    return str

