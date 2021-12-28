def solution(n):
    if n > 5*(10**13) or n <= 0:
        n = int(input("50000000000000이하의 양의 정수를 입력하세요 : "))
        solution(n)
    else:
        i = 2
        while i <= n:
            if i**2 == n:
                return (i+1)**2
                break
            else:
                i += 1
        return -1