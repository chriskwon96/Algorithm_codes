di = [0, -1, 0, +1]
dj = [+1, 0, -1, 0]

def change_to_zero(border_list):
    for i, j in border_list:
        matrix[i][j] = 0

def create_borderlist(q):
    border_list = []
    while q:
        x, y = q.pop(0)
        visited[x][y] = 1
        for d in range(4):
            next_x, next_y = x+di[d], y+dj[d]
            if 0<=next_x<N and 0<=next_y<M and visited[next_x][next_y] == 0:
                if matrix[next_x][next_y] == 1:
                    border_list.append((next_x, next_y))
                else:
                    q.append((next_x, next_y))
                visited[next_x][next_y] = 1
    return border_list

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

total_time = 0
last_cheese = 0
 
border_list = [(0,0)]

while border_list:
    last_cheese = len(border_list)
    total_time += 1
    
    new_border_list = create_borderlist(border_list)
    change_to_zero(new_border_list)
    border_list = new_border_list


print(total_time-1)
print(last_cheese)




