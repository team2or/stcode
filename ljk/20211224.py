#문자열 내 마음대로 정렬하기
strings=["abce", "abcd", "cdx"]

def solutioin(strings, n):
    answer=[]
    index_alph=[]
    strings.sort()
    for string in strings:
        index_alph.append(string[n])
    index_alph.sort()
    for alph in index_alph:
        for string in strings:
            if string[n]==alph:
                if string not in answer:
                    answer.append(string)
    return answer


def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    return sorted(strings, key=lambda x: x[n])

strings = ["sun", "bed", "car"] 
print(strange_sort(strings, 1))


strings=["abce", "abcd", "cdx"]
def solution(strings, n):
    str=[]
    for i in strings:
        str.append(i[n]+i) #문자열 앞에 추가해도 정렬에는 이상없음
    str.sort()
    return [i[1:] for i in str]

solution(strings, 2)

