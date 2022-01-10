#없는 숫자 더하기


def solution(test_serial):
    number=[0,1,2,3,4,5,6,7,8,9]
    for i in test_serial:
        if i in number:
            number.remove(i)
    return sum(number)

solution([1,2,3,4,5,6,7,8])


def solution(numbers):
    answer=0
    for i in range(1,10):
        if i not in numbers:
            answer+=i
    return answer
solution([1,2,3,4,5,6,7,8])
#다른 풀이
def solution(numbers):
    return 45 - sum(numbers)