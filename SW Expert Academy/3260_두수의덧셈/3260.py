T = int(input())

for t in range(1, T+1):
    A, B = map(int, input().split())
    result = int(A+B)
    print('#{} {}'.format(t, result))