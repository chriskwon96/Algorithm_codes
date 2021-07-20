def solution(priorities, location):
    N = len(priorities)
    for i in range(N):
        priorities[i] = (priorities[i], i)
    turn = 0
    while priorities:
        turn += 1
        pri, idx = priorities.pop(0)
        flag = 1
        for x,y in priorities:
            if x > pri:
                priorities.append((pri, idx))
                turn -= 1
                flag = 0
                break
        if flag and idx == location: return turn

    return turn


print(solution([2,1,3,2], 2))
print(solution([1,1,9,1,1,1], 0))



