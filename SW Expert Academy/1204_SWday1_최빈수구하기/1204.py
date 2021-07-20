T = int(input())

for t in range(1, T+1):
    N = int(input())
    scores = list(map(int, input().split()))
    students = [0]*101

    for score in scores:
        students[score] += 1

    maxes = []
    for i in range(len(students)):
        if students[i] == max(students):
            maxes.append(i)

    result = max(maxes)


    print('#{} {}'.format(t, result))
