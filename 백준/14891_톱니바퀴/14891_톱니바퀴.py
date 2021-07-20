
def turn(w, di):
    if di > 0: #시계방향
        temp = w[7]
        for i in range(7,0,-1):
            w[i] = w[i-1]
        w[0] = temp
    else: #반시계
        temp = w[0]
        for i in range(7):
            w[i] = w[i+1]
        w[7] = temp


wheels = [list(map(int, input())) for _ in range(4)]

k = int(input())
for _ in range(k):
    w_num, dir = map(int, input().split())
    poles = [0,0,0]
    for i in range(3): #극확인
        if wheels[i][2] != wheels[i+1][6]:
            poles[i] = 1
    turn(wheels[w_num-1], dir) #일단 내꺼 턴

    if w_num == 1:
        if poles[0]:
            turn(wheels[1], -dir)
            if poles[1]:
                turn(wheels[2], dir)
                if poles[2]:
                    turn(wheels[3], -dir)
    elif w_num == 2:
        if poles[0]: # 1-2 바퀴
            turn(wheels[0], -dir)
        if poles[1]: # 2-3 wheel
            turn(wheels[2], -dir)
            if poles[2]: #3-4
                turn(wheels[3], dir)
    elif w_num == 3:
        if poles[2]: # 3-4
            turn(wheels[3], -dir)
        if poles[1]: # 2-3
            turn(wheels[1], -dir)
            if poles[0]: #1-2
                turn(wheels[0], dir)
    else:
        if poles[2]:
            turn(wheels[2], -dir)
            if poles[1]:
                turn(wheels[1], dir)
                if poles[0]:
                    turn(wheels[0], -dir)
score = 0
for i in range(4):
    if wheels[i][0]:
        score += 2**i
print(score)


