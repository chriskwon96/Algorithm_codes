T = int(input())
for t in range(1, T+1):
    oriD, A_vel, B_vel, F_vel = map(int, input().split()) #D: distance F: 파리속력
    #A, B의 초기값 설정
    A = 0
    B = oriD
    F = 0
    D = oriD
    total_time = 0
    total_dis = 0

    while total_time < oriD / (A_vel+B_vel) : #A랑 B랑 만나기 전까지
        if F == A: #A랑 F랑 만나면
            time = D / (F_vel + B_vel) #파리랑 B랑 만나는 시간 구하기
            A = A + (A_vel * time)  # A, B위치
            B = B - (B_vel * time)
            F = B
        else:
            if F == B: #파리랑 B랑 만나면
                time = D / (F_vel + A_vel) #파리랑 A랑 만나는 시간구하기
                A = A + (A_vel * time)  # A, B위치
                B = B - (B_vel * time)
                F = A

        D = B - A
        total_time += time
        total_dis += F_vel * time

    print('#{} {}'.format(t, total_dis))