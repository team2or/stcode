def solution(numbers):
    answer = []
    for idx in range(len(numbers)):
        for i in numbers[idx + 1:]:
            num = numbers[idx] + i
            if num not in answer:
                answer.append(num)

    return sorted(answer)