#프로그래머스_SQL
#복습
#동명 동물수 찾기
#https://programmers.co.kr/learn/courses/30/lessons/59041
#두번이상 쓰인 이름: count(name) > 1인 이름 출력
#WHERE, GROUP BY, HAVING, ORDER BY 순으로 쓰임
SELECT NAME, COUNT(NAME) FROM ANIMAL_INS WHERE NAME IS NOT NULL GROUP BY NAME
HAVING COUNT(NAME) > 1 ORDER BY NAME;

#방문길이
#https://programmers.co.kr/learn/courses/30/lessons/49994
#왜 visited가 리셋되는거지?!...
dirs = "ULURRDLLU"
visited = []
p = [0,0]
for d in dirs:
    if d == "U" and p[1] < 5:
        p[1] += 1
    elif d == "D" and p[1] > -5:
        p[1] -= 1
    elif d == "R" and p[0] < 5:
        p[0] += 1
    elif d == "L" and p[0] > -5:
        p[0] -= 1
    print(p)
    if p not in visited:
        visited.append(p)
print(visited)

#이전에 방문한 위치를 카운트안했던 거였는데
#문제를 다시보니 "처음 걸어본 길의 길이"를 구하는 거 였음
dirs = "LULLLLLLU"
visited = set()
x,y=0,0
for d in dirs:
    if d == "U" and y < 5:
        visited.add((x,y))
        y += 1
    elif d == "D" and y > -5:
        visited.add((x,y))
        y -= 1
    elif d == "R" and x < 5:
        visited.add((x,y))
        x += 1
    elif d == "L" and x > -5:
        visited.add((x,y))
        x -= 1
print(visited)
print(len(visited))

#답안
#https://roomedia.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%B0%A9%EB%AC%B8-%EA%B8%B8%EC%9D%B4-SummerWinter-Coding2018-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A7%91%ED%95%A9
#이전 위치와 이동한 위치를 함께 add
#이미 간 길은 제거 set으로 제외
dirs = "LULLLLLLU"
visit = set()
x = 0; y = 0
for d in dirs:
    if d == 'U' and y < 5:
        visit.add(((x, y), (x, y+1)))
        y += 1
        
    elif d == 'D' and y > -5:
        visit.add(((x, y-1), (x, y)))
        y -= 1
        
    elif d == 'R' and x < 5:
        visit.add(((x, y), (x+1, y)))
        x += 1
        
    elif d == 'L' and x > -5:
        visit.add(((x-1, y), (x, y)))
        x -= 1
print(visit)
