
def paper_cut(start_i, start_j, n):
    global total_paper
    start_val = matrix[start_i][start_j]

    for i in range(start_i, start_i+n):
        for j in range(start_j, start_j+n):

            if matrix[i][j] != start_val:
                # 9등분하기
                for third_i in range(3):
                    for third_j in range(3):
                        new_i = start_i + third_i * n//3
                        new_j = start_j + third_j * n//3
                        paper_cut(new_i, new_j, n//3)
                return

    # 모두 같다면
    total_paper[start_val+1] += 1


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
total_paper = [0, 0, 0]

paper_cut(0, 0, N)

for idx in range(3):
    print(total_paper[idx])

