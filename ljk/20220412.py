#네트워크
def dfs(x,computers):
    computers[x][x]=2
    for i in range(len(computers[x])):
        if computers[x][i]==1 and computers[i][i]!=2:
            dfs(i,computers)

def solution(n, computers):
    answer = 0

    for i in range(n):
        if computers[i][i]==1:
            dfs(i, computers)
            answer+=1

    return answer
