#해커랭크
#복습
#The Blunder
#https://www.hackerrank.com/challenges/the-blunder/problem?isFullScreen=true
SELECT ceil(avg(Salary)-avg(replace(Salary, 0, ''))) FROM Employees;

#프로그래머스
#[3차] 파일명 정렬
#https://programmers.co.kr/learn/courses/30/lessons/17686
#참고답안: https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-%ED%8C%8C%EC%9D%BC%EB%AA%85-%EC%A0%95%EB%A0%AC-Python
#head, number, tail을 먼저 선언해 주고, 한 파일명이 완료되었을 때 다시 포맷해줘야 함
files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
files_split = []
head, number, tail = '', '', ''
for file in files:
    for i in range(len(file)):
        if file[i].isdigit():
            head = file[:i]
            number = file[i:]
            for num in range(len(number)):
                if not number[num].isdigit():
                    tail = number[num:]
                    number = number[:num]
                    break
            files_split.append([head, number, tail])
            head, number, tail = '', '', ''
            break
print(files_split)
files_split = sorted(files_split, key=lambda x:(x[0].lower(), int(x[1])))
print([''.join(files) for files in files_split])

#다른 답안
#정규표현식: "\d+"는 '하나 혹은 그 이상 연결된 숫자`
#
#https://velog.io/@geonhwi/%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D-2
import re
def solution(files):
    #먼저 숫자 순으로 정렬 후(number)
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    #앞의 문자 순으로 정렬(head)
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    return b

solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])