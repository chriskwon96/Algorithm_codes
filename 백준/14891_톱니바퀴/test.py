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
w = [1,2,3,4,5,6,7,8]
turn(w, -1)

print(w)