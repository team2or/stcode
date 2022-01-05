def solution(n, m):
    answer = [0, 0]
    for i in range(1, max(n, m)):
        if n%i == 0 and m%i == 0:
            answer[0] = i
            answer[1] = (n//i)*(m//i)*i
    return answer