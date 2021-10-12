di = [0, -1, 0, +1]
dj = [+1, 0, -1, 0]

# 터트린 공을 '.' 으로 변환하는 함수
def change_2_dot(pop_list):
    for coor in pop_list:
        matrix[coor[0]][coor[1]] = '.'
    
# 공을 터트린 후 남은 공을 아래로 정리하는 함수
def fall_down():
    for j in range(6):
        for i in range(11, 0, -1):
            if matrix[i][j] == '.':
                for n_i in range(i-1, -1, -1):
                    if matrix[n_i][j] != '.':
                        matrix[i][j] = matrix[n_i][j]
                        matrix[n_i][j] = '.'
                        break


# 한가지 색에 대한 터질 공 그룹의 좌표를 반환하는 함수 
def create_group(color, start_x, start_y):
    global pop_count, pop_flag

    pop_list = [(start_x, start_y)]
    q = [(start_x, start_y)]

    while q:
        x, y = q.pop(0)
        visited[x][y] = 1
        for d in range(4):
            next_x, next_y = x+di[d], y+dj[d]

            if 0<=next_x<12 and 0<=next_y<6 and visited[next_x][next_y] == 0:
                if matrix[next_x][next_y] == color:
                    visited[next_x][next_y] = 1
                    q.append((next_x, next_y))
                    pop_list.append((next_x, next_y))

    if len(pop_list) >= 4:
        total_pop_list.extend(pop_list)
        pop_flag = True

    return


matrix = [list(input()) for _ in range(12)]

pop_flag = True
pop_count = 0

while pop_flag:
    pop_flag = False
    total_pop_list = []
    visited = [[0]*6 for _ in range(12)]

    # 한번의 시도에 터트릴 공의 그룹을 모두 찾는다
    for i in range(12):
        for j in range(6):
            if matrix[i][j] != '.' and visited[i][j] == 0:
                create_group(matrix[i][j], i, j)

    # 터트릴게 있다면 
    # 1. 터트려야할 모든 공의 좌표에 대해 '.' 으로 변환 후 
    # 2. 아래로 정리한다
    # 3. 연쇄 반응 +1 
    if pop_flag:
        change_2_dot(total_pop_list)
        fall_down()
        pop_count += 1

print(pop_count)

