#해커랭크
#복습
#Challenges
#https://www.hackerrank.com/challenges/challenges/problem?isFullScreen=true
#먼저 GROUP BY로 묶은 결과 값을 가지고 조건을 사용해야할 때 HAVING을 사용함
SELECT H.hacker_id, H.name, count(C.hacker_id) AS total_challenge FROM Challenges C LEFT JOIN Hackers H ON C.hacker_id=H.hacker_id GROUP BY H.hacker_id, H.name 
HAVING total_challenge IN (SELECT total FROM (SELECT count(*) as total FROM Challenges GROUP BY hacker_id) as tab1 GROUP BY total HAVING count(total)=1)
OR total_challenge = (SELECT count(*) as total FROM Challenges GROUP BY hacker_id ORDER BY total DESC LIMIT 1)
ORDER BY total_challenge DESC, hacker_id;


#프로그래머스
#해시
#베스트앨범
#https://programmers.co.kr/learn/courses/30/lessons/42579
genres = ["classic", "pop", "classic", "classic", "pop"]	
plays = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    music = {}
    for i in range(len(genres)):
        if genres[i] not in music:
            music[genres[i]] = [[plays[i],i]]
        else:
            music[genres[i]] += [[plays[i],i]]

    #가장많이 재생된 수로 정렬하기/각 장르별 play 수 구하기
    music_list = []
    for m, v in music.items():
        music[m] = sorted(v, reverse=True)
        music_list.append([sum([i[0] for i in v]), m])

    #가장 많이 재생된 장르로 정렬
    music_list.sort(key=lambda x:x[0], reverse=True)

    #가장 많이 재생된 장르 순으로 가장많이 play된 노래번호 구하기
    answer = []
    for k in music_list:
        play_list = sorted([m for m in music[k[1]]], key=lambda x:(-x[0],x[1]))
        answer.append([m[1] for m in play_list][:2])

    return sum(answer,[])

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
#같은 장르 중 play횟수가 같으면 번호가 낮은 순으로 앨범에 넣어야 함
solution(["classic", "pop", "classic", "classic", "pop"], [150, 600, 150, 800, 2500])
print(solution(["classic", "pop", "classic", "classic", "pop", "test"], [500, 600, 150, 800, 2500, 100]))
print(solution(["classic"], [300]))

#다른 답안
def solution(genres, plays):
    answer = []

    #각 장르별 번호와 play횟수를 사전형으로 만듦
    dic1 = {}
    #각 장르별 play 횟수 합계
    dic2 = {}

    #zip으로 두 list를 묶어 출력할 수 있음
    #enumerate으로 출력 횟수를 자동으로 카운트한 수를 구할 수 있음
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    #가장 많이 play된 장르 구하기
    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        #가장 많이 play된 장르 순으로 가장많이 play된 노래번호 구하기
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer