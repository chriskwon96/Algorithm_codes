






def solution(participant, completion):
    par = dict()
    for c in completion:
        if c in par:
            par[c] += 1
        else:
            par[c] = 1

    for p in participant:
        if p not in par or par[p] == 0:
            return p
        else:
            par[p] -= 1

print(solution())


