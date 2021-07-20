T = int(input())
for t in range(1, T+1):
    num_stu, assign = map(int, input().split())
    students = list(map(int, input().split()))
    print('#{}'.format(t), end = ' ')
    for i in range(1, num_stu+1):
        if i not in students:
            print(i, end = ' ')
    print()
