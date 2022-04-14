#베스트앨범

def solution(genres, plays):
    answer = []
    byGenre={genres[i]:0  for i in range(len(plays))}
    withnum = {}
    for i in range(len(genres)):
        byGenre[genres[i]] += plays[i]
        withnum[genres[i]] = withnum.get(genres[i], []) + [(plays[i], i)]

    genresort = sorted(byGenre.items(), key = lambda x: x[1], reverse = True)

    """
    sort by album:play
    """
    print(genresort)
    print(withnum)
    for (genre, total_play) in genresort:
        withnum[genre] = sorted(withnum[genre], key=lambda x: (-x[0], x[1]))
        answer += [idx for (play,idx) in withnum[genre][:2]]
        print(withnum[genre])
        print(withnum[genre][:2])
    print(answer)
    return answer
solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])