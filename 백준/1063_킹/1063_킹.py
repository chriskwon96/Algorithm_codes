def stone_check(di, dj, i ,j):
    if [i+di, j+dj] == stone:
        if 0 <= i+2*di < 8 and 0 <= j + 2*dj <8: # 돌을 움직일 수 있다면
            stone[0] += di
            stone[1] += dj
            king[0] += di
            king[1] += dj
    else:
        king[0] += di
        king[1] += dj


king, stone, N = input().split()

king = [int(king[1])-1, ord(king[0])-ord("A")]
stone = [int(stone[1])-1, ord(stone[0]) - ord("A")]

dir_chr = ["R", "L", "B", "T", "RT", "LT", "RB", "LB"]
dir = [(0, +1), (0, -1), (-1, 0), (+1, 0), (+1, +1), (+1, -1), (-1, +1), (-1,-1)]

for _ in range(int(N)):
    move = input()
    di, dj = dir[dir_chr.index(move)]
    if 0 <= di + king[0] < 8 and 0 <= dj + king[1] < 8:
        flag = stone_check(di, dj, king[0], king[1])

print(chr(king[1]+65)+str(king[0]+1))
print(chr(stone[1]+65)+str(stone[0]+1))





