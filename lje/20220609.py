#해커랭크
#복습
#Weather Observation Station 18
#https://www.hackerrank.com/challenges/weather-observation-station-18/problem?isFullScreen=true
SELECT round((max(LAT_N)-min(LAT_N)) + (max(LONG_W)-min(LONG_W)),4) FROM STATION; 


#프로그래머스
#[3차] 방금그곡
#https://programmers.co.kr/learn/courses/30/lessons/17683
m = "ABCDEFG"
musicinfos = 	["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
m = "CC#BC"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]

# "#"이 들어간 악보를 한단어로 변경
def replace(m):
    for a,b in zip(["A#", "C#", "D#", "F#", "G#"], ["a","c","d","f","g"]):
        m = m.replace(a,b)
    return m

def solution(m, musicinfos):
    answer = []
    m = replace(m)
    no = 1
    for i in musicinfos:
        s,e,title,music = i.split(',')
        music = replace(music)
        #시간을 모두 분으로 변환
        time = (int(e[:2]) - int(s[:2]))*60 + (int(e[3:])-int(s[3:]))

        #시간과 음악길이 비교하여 길면 자르고 짧으면 덧붙임
        if len(music) >= time:
            music = music[:time]
        else:
            #몫과 나머지로 시간 길이만큼 악보 늘림
            q, r =divmod(time, len(music))
            music = music*q + music[:r]
        if m in music:
            answer.append([no, time, title])
        no += 1

    if len(answer) != 0:
        answer = sorted(answer, key=lambda x: (-x[1], x[0]))
        return answer[0][2]
    return "(None)"

#참고
#https://eda-ai-lab.tistory.com/506
#https://mingchin.tistory.com/135