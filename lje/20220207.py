# 프로그래머스_SQL
# 역순으로 정렬하기
# https://programmers.co.kr/learn/courses/30/lessons/59035
SELECT NAME, DATETIME FROM ANIMAL_INS ORDER BY ANIMAL_ID DESC

# 여러 기준으로 정렬하기
# https://programmers.co.kr/learn/courses/30/lessons/59404
SELECT ANIMAL_ID, NAME, DATETIME FROM ORDER BY NAME, DATETIME


# 영어 끝말잇기
# https://programmers.co.kr/learn/courses/30/lessons/12981
def solution(n, words):
    answer = []
    re = []
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in re:
            answer.append((i % n)+1)
            answer.append((i//n)+1)
        else:
            re.append(words[i-1])
    if answer == []:
        answer = [0, 0]
    return answer


solution(3, ["tank", "kick", "know", "wheel",
         "land", "dream", "mother", "robot", "tank"])
solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage",
         "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])
solution(2,	["hello", "one", "even", "never", "now", "world", "draw"])

# 다른 답안
# https://velog.io/@insutance/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Python-%EC%98%81%EC%96%B4-%EB%81%9D%EB%A7%90%EC%9E%87%EA%B8%B0


def solution(n, words):
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
            return [(i % n)+1, (i//n)+1]
    else:
        return [0, 0]
