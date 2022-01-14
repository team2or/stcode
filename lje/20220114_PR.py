#프로그래머스
#k번째 수
#https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for i in commands:
        split = sorted(array[(i[0]-1):i[1]])
        answer.append(split[i[2]-1])
    return answer
solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])

#크레인 인형뽑기 게임
#https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    a = []
    answer = 0
    for i in moves:
        for j in board:
            if j[i-1] != 0:
                if len(a) == 0 or a[-1] != j[i-1]:
                    a.append(j[i-1])
                    j[i-1] = 0
                #a 리스트 맨마지막 숫자와 다음에 들어갈 숫자가 같으면,
                #마지막 숫자 리스트에서 제거 / 뽑은 자리 숫자 0처리
                else:
                    answer += 2
                    j[i-1] = 0 #뽑은 숫자 0처리
                    del a[-1]
                break
    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])