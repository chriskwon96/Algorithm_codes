import itertools

T = int(input())
for t in range(1, T+1):
    N = int(input())
    result = []
    matrix = [list(map(int, input().split())) for _ in range(N)]
    combs = list(itertools.combinations(list(range(N)), N//2))

    for comb in combs:
        A = 0
        B = 0
        for i in range(N):
            for j in range(N):
                if i in comb and j in comb:
                    A += matrix[i][j]
                if i not in comb and j not in comb:
                    B += matrix[i][j]
        result.append(abs(A-B))

    print('#{} {}'.format(t, min(result)))
