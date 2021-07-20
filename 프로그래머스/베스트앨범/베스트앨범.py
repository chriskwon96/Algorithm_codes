


def solution(genres, plays):
    genre_plays = dict()
    N = len(genres)
    for i in range(N):
        if genres[i] not in genre_plays:
            genre_plays[genres[i]] = [(plays[i], i)]
        else:
            genre_plays[genres[i]].append((plays[i], i))

    for val in genre_plays.values():
        val.sort(reverse=True)
    mylist = sorted(list(genre_plays.items()), key=lambda x:sum(x[1][0]), reverse=True)
    ans = []
    for i in range(len(mylist)):
        if len(mylist[i][1]) == 1:
            ans.append(mylist[i][1][0][1])
        else:
            ans.append(mylist[i][1][0][1])
            ans.append(mylist[i][1][1][1])
    return ans


solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
