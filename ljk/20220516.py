def solution(s):
    answer = ''
    s= s.split(' ')
    for i in s:
        if i == '':
            answer+=' '
            continue
        if i[0].isdigit():
            answer+=i.lower()
        elif i[0].isalpha():
            answer+= i[0].upper()
            answer+= i[1:].lower()
        answer+=' '

    return answer[:-1]

print(solution( "a a a a a a a a a a "))

