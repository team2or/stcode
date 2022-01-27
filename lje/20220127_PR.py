#프로그래머스
#다트게임
#https://programmers.co.kr/learn/courses/30/lessons/17682
def solution(dartResult):
    score = []
    dartResult = dartResult.replace('10', 't')
    for i in dartResult:
        if i.isdigit():
            score.append(int(i))
        elif i == 't':
            score.append(10)
        elif i == 'S':
            num = score.pop()
            score.append(num**1)
        elif i == 'D':
            num = score.pop()
            score.append(num**2)
        elif i == 'T':
            num = score.pop()
            score.append(num**3)
        elif i == '*':
            score[-1] *= 2
            if len(score) > 1:
                score[-2] *= 2
        else:
            score[-1] *= -1
    return sum(score)

solution("1S2D*3T")
solution("1D2S#10S")
solution("1D2S0T")
solution("1S*2T*3S")

#다른 답안
#https://latte-is-horse.tistory.com/136
def solution(dartResult):
    stack = []
    #'10' -> 'A'로 변경
    dartResult = dartResult.replace("10", "A")
    bonus = {'S': 1, 'D': 2, 'T': 3}
    
    for i in dartResult:
        #i가 숫자이거나 A면 숫자로 변경 후 stack리스트에 추가
        if i.isdigit() or i=='A':
            stack.append(10 if i == 'A' else int(i))
        #i가 'S', 'D', 'T'중 하나면
        elif i in ('S', 'D', 'T'):
            #stack리스트 맨마지막 숫자 추출 후 제곱
            num = stack.pop()
            stack.append(num ** bonus[i])
        elif i == '#':
            stack[-1] *= -1
        elif i == '*':
            num = stack.pop()
            #위의 숫자 추출 후 리스트에 아직 숫자가 남아있다면
            if len(stack):
                #그 전 숫자까지 *2해줌
                stack[-1] *= 2
            stack.append(2 * num)
    return sum(stack)

#약수의 개수와 덧셈
#https://programmers.co.kr/learn/courses/30/lessons/77884
def solution(left, right):
    answer = 0
    l = []
    for i in range(left,right+1):
        count = 0
        for j in range(1,i+1):
            if i%j == 0:
                count += 1
        if count%2==0:
            answer += i
        else:
            answer -= i
    return answer
solution(13,17)
solution(24,27)