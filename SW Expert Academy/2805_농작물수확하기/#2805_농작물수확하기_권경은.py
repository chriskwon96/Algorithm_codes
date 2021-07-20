T= int(input())

for t in range(1,T+1):

    N = int(input())

    total = 0
    matrix =[list(map(int, list(input()))) for _ in range(N)]


    for i in range(((N-1)//2)+1):
        if i == (N-1)/2:
            total += sum(matrix[i])

        else:
            total += sum(matrix[i][int(((N-1)/2) - i) : int((N-1)/2 +i+1)])
            total += sum(matrix[N-1-i][int((N-1)/2 - i) : int((N-1)/2 +i+1)])

    print('#{} {}'.format(t,total))
