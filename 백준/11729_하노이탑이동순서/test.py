def hanoi(N, beg, aux, end):
    global cnt

    if N == 1:
        cnt += 1
        steps.append([beg, end])
    else:
        hanoi(N-1, beg, end, aux)
        hanoi(1, beg, aux, end)
        hanoi(N-1, aux, beg, end)

N = int(input())
steps =[]
cnt = 0
hanoi(N, 1, 2, 3)
print(cnt)
for step in steps:
    for i in step:
        print(i, end = ' ')
    print()