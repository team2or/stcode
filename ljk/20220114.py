#k번째 수

def solution(array, commands):
    answer=[]
    for i,j,k in commands:
        array_=array[i-1:j]
        array_.sort()
        answer.append(array_[k-1])
    return answer

solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])

#크레인 인형뽑기 게임

def crain(board, moves):
    block=[]
    answer=0
    for move in moves:
        cnt=0
        for _ in range(len(board)):
            if board[cnt][move-1]==0:
                cnt+=1
            elif board[cnt][move-1]!=0:
                block.append(board[cnt][move-1])
                board[cnt][move-1]=0
                break
        print(block)
        if len(block)>=2 and block[-1]==block[-2]:
            block.pop()
            block.pop()
            answer+=2
    return answer

crain([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])
424
for i in range(10):
    print(i)
    if i ==4:
        break