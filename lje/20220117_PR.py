#프로그래머스
#수박수박수박수박수박수?
#https://programmers.co.kr/learn/courses/30/lessons/12922
def solution(n):
    answer = ''
    for i in range(n):
        if i%2 == 0:
            answer += '수'
        else:
            answer += '박'
    return answer

solution(3)
solution(4)

#키패드 누르기
#https://programmers.co.kr/learn/courses/30/lessons/67256
def solution(numbers, hand):
    answer = ''
    #왼손,오른손 시작 위치
    left = '*'
    right = '#'
    #키패드 좌표 표시
    kp = {1:(0,0),2:(0,1),3:(0,2),
        4:(1,0),5:(1,1),6:(1,2),
        7:(2,0),8:(2,1),9:(2,2),
        '*':(3,0),0:(3,1),'#':(3,2)}
    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            left = i
        elif i in [3,6,9]:
            answer += 'R'
            right = i
        elif i in [2,5,8,0]:
            num = kp[i]
            rnow = kp[right]
            lnow = kp[left]
            #왼손, 오른손과 현재위치 거리 구하기
            rdist = abs(num[0]-rnow[0]) + abs(num[1]-rnow[1])
            ldist = abs(num[0]-lnow[0]) + abs(num[1]-lnow[1])
            #현재위치에서 오른손 거리가 멈 -> 왼손으로 누름
            if rdist > ldist:
                answer += 'L'
                left = i
            #현재위치에서 왼손 거리가 멈 -> 오른손으로 누름
            elif rdist < ldist:
                answer += 'R'
                right = i
            #현재위치에서 오른손 == 왼손 -> 어느 손잡이냐에 따라 다름
            else:
                if hand == 'left':
                    answer += 'L'
                    left = i
                else:
                    answer += 'R'
                    right = i
    return answer

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],'right')
solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],'left')
solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],'right')