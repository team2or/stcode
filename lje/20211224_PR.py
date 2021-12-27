# 프로그래머스
# 문자열 내 마음대로 정렬하기
## strings 한번더 sorted 해야 함.
def solution(strings, n):
    word = sorted(sorted(strings), key = lambda x : (x[n], x[n+1]))
    return word

solution(["abce", "abcd", "cdx"], 1)