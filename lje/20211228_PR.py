#프로그래머스

#문제1
#자연수 뒤집어 배열로 만들기
#https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    answer = []
    for i in str(n):
        answer.append(int(i))
    answer = list(reversed(answer))
    return answer


#문제2
#2016년
#https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    day = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    num = 0
    for i in range(a):
        if i == a-1:
            num += b
        else:
            num += month[i]
    answer = day[(num%7)-1]
    return answer
