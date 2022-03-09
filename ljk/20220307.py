#타겟 넘버
def solution(numbers, target):
    n = len(numbers)
    answer = 0
    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
    dfs(0,0)
    return answer



if __name__=="__main__":
    numbers=[1, 1, 1, 1, 1]
    target=3
    ans=solution(numbers, target)
    print(ans)



