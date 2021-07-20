T = int(input())
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for t in range(1, T+1):
    N, K = map(int, input().split())
    #N: num of students K: target student
    students = [0] * N
    for n in range(N):
        mid, final, assign = map(int, input().split())
        total = (0.35*mid) + (0.45*final) + (0.2*assign)
        students[n] = total
        if n+1 == K:
            target = total

    #K가 몇등인지
    students.sort()
    students.reverse()
    rank = students.index(target)
    i = 0

    while rank >= N // 10:
        rank = rank - N//10
        i += 1
        if i == 9:
            break
    my_grade = grades[i]
    print('#{} {}'.format(t, my_grade))