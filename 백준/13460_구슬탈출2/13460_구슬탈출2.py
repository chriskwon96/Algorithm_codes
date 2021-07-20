di = [0, -1, 0, +1]
dj = [+1, 0, -1, 0]


def tilt(r_x, r_y, b_x, b_y, k):
    nr_x, nr_y, nb_x, nb_y = r_x+di[k], r_y+dj[k], b_x+di[k], b_y+dj[k]
    flag_R, flag_B, fail_B, goal_R = 0,0,0,0

    while matrix[nb_x][nb_y] != '#':
        if matrix[nb_x][nb_y] == 'O':
            fail_B = 1
            break
        elif [nb_x, nb_y] == [r_x,r_y]:
            flag_B = 1
        nb_x += di[k]
        nb_y += dj[k]

    if not fail_B:   #B가 들어가면 그냥 다 실행하지마
        while matrix[nr_x][nr_y] != '#':
            if matrix[nr_x][nr_y] == 'O':
                goal_R = 1
                break
            elif [nr_x, nr_y] == [b_x, b_y]:
                flag_R = 1
            nr_x += di[k]
            nr_y += dj[k]

        if not goal_R: #A도 안들어가고 B도 안들어감
            if flag_R: #만약 A앞에 B가 잇다면
                return [nr_x-(2*di[k]), nr_y-(2*dj[k]), nb_x-di[k], nb_y-dj[k]]
            if flag_B: #만약 B앞에 A가 있다면
                return [nr_x-di[k], nr_y-dj[k], nb_x-(2*di[k]), nb_y-(2*dj[k])]
            else: #둘다 안겹친다면
                return [nr_x-di[k], nr_y-dj[k], nb_x-di[k], nb_y-dj[k]]
        else: #A만 들어가고 B는 안들어감
            return 1



def bfs():
    while q:
        # print(q)
        r_x, r_y, b_x, b_y, cur_step = q.pop(0)
        if cur_step < 10: # 현재가 10번째 미만일때만 기울어봐
            for k in range(4):
                #기운 후 좌표 찾기
                result = tilt(r_x, r_y, b_x, b_y, k)
                # print(result)
                if result == 1:
                    return cur_step+1
                elif result: #1이 아닌 리턴값이 있다면
                    if result not in v:
                        v.append(result)
                        rresult = result[::]
                        rresult.append(cur_step + 1)
                        q.append(rresult)

    return -1


N, M = map(int, input().split())
matrix = list(list(input()) for _ in range(N))
v = []
q = []
step = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'R':
            red_i, red_j = i, j
        if matrix[i][j] == 'B':
            blue_i, blue_j = i, j

v.append([red_i, red_j, blue_i, blue_j])
q.append([red_i, red_j, blue_i, blue_j, step])


ans = bfs()
print(ans)

