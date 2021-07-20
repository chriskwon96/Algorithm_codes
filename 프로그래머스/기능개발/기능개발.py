from math import ceil
def solution(progresses, speeds):
    N = len(progresses)
    days = [0]*N
    for i in range(N):
        days[i] = ceil((100 - progresses[i])/speeds[i])

    ans = []
    i = 0
    while days:
        start = days.pop(0)
        skill = 1
        while days:
            if days[0] <= start:
                days.pop(0)
                skill += 1
            else:
                ans.append(skill)
                break

        if not days:
            ans.append(skill)

    return ans

print(solution([93,30,55], [1,30,5]))
print(solution([99,1],[1,99]))
print(solution([95, 95, 95, 95], [4, 3, 2, 1]))
