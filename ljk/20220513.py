
def solution(brackets):

    answer = 0
    for i in range(len(brackets)):
        p = brackets
        while len(brackets) >1:
            start_n = len(brackets)
            brackets = brackets.replace('{}', '')
            brackets = brackets.replace('[]', '')
            brackets = brackets.replace("()", '')
            end_n = len(brackets)
            if start_n == end_n or end_n ==0:
                if end_n == 0:
                    answer += 1
                break

        brackets = p[1:]+p[0]
    return answer

print(solution('[][]{}'))

