from collections import deque
def solution(n):
    top = [[0]*n for _ in range(n)]
    x, y = -1, 0
    num = 1
    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:  # 아래
                x += 1
            elif i % 3 == 1:  # 오른쪽
                y += 1
            elif i % 3 == 2:  # 위쪽 대각선
                x -= 1
                y -= 1
            top[x][y] = num
            num += 1
    answer = []
    for i in top:
        for j in i:
            if j:
                answer.append(j)
    print(answer)
    return answer
solution(4)