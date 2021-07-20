dj = [0, -1, 0, +1]
di = [+1, 0, -1, 0]

def move(a,b,dir):
    n_coor = (a+di[dir], b+dj[dir])
    n_dir = (dir+1)%4
    return n_coor, n_dir


N = int(input())

final_dragon = []
sq = 0
for _ in range(N):
    x,y,d,g = map(int, input().split())
    dragon = [(x,y)]
    dir = [d]
    # 초기값 설정 => generation == 0
    tail = dragon[-1]
    n_coor, n_dir = move(tail[0], tail[1], dir[-1])
    dragon.append(n_coor)
    dir.append(n_dir)
    cur_gen = 0

    while cur_gen < g:
        for i in range(len(dir)-1, 0, -1):
            tail = dragon[-1]
            n_coor, n_dir = move(tail[0], tail[1], dir[i])
            dragon.append(n_coor)
            dir.append(n_dir)
        cur_gen += 1
    final_dragon.extend(dragon)


final_dragon = set(final_dragon)
for coor in final_dragon:
    # 왼쪽 상위 좌표라고 가정
    x, y = coor
    if (x+1,y) in final_dragon and (x,y+1) in final_dragon and (x+1,y+1) in final_dragon:
        sq += 1
print(sq)



