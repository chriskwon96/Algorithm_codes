def solution(dirs):
    def moves(x, y, m):
        if m == 'U':
            return [x-1, y]
        elif m == 'L':
            return [x, y-1]
        elif m == "R":
            return [x, y+1]
        else:
            return [x+1, y]

    visited = []
    pos = (0,0)
    cnt = 0

    for i in dirs:
        x, y = pos[0], pos[1]
        new_x, new_y = moves(pos[0], pos[1], i)
        if -5<=new_x<=5 and -5<=new_y<=5:
            new_pos = (new_x, new_y)
            path = {pos, new_pos}
            if path not in visited:
                visited.append(path)
                cnt += 1
            pos = new_pos

    return cnt









