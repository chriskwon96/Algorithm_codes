dirs = [(+1, 0), (0, -1), (-1, 0), (0, +1)]

N = int(input())
moves = list(input())

x,y = 0,0

cnt = 0
coords = [[0,0]]

for i in range(N):
    if moves[i] == "F":
        x += dirs[cnt%4][0]
        y += dirs[cnt%4][1]
        coords.append([x,y])
        cnt %= 4
    elif moves[i] == "L":
        cnt -= 1
    elif moves[i] == "R":
        cnt += 1

coords.sort(key=lambda x:x[0])
max_x, min_x = coords[-1][0], coords[0][0]
coords.sort(key=lambda x:x[1])
max_y, min_y = coords[-1][1], coords[0][1]

interval_x = max_x-min_x +1
interval_y = max_y-min_y +1

matrix = [["#"]*interval_y for _ in range(interval_x)]

for coord in coords:
    matrix[coord[0]+abs(min_x)][coord[1]+abs(min_y)] = "."

for m in matrix:
    print("".join(m))