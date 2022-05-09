
def solution(land):
    n = len(land)
    for i in range(1,n):
        for j in range(4):
            land[i][j] += max(land[i-1][k] for k in range(4) if k!=j )
    answer = max(land[n-1])
    return answer

print(solution([[1,2,3,5],
[5,6,7,100],
[4,3,2,1]]))