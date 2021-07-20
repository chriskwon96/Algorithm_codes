

def play(nights, n):
    global max_nights, flag

    if flag:
        if guilt[mafia]==0 or n == 1 : #마피아가 죽었다면 아니면 마피아 빼고 다죽었다면
            if n == 1: #마피아가 승리한 경우 == 최고
                flag = 0
            if nights > max_nights:
                max_nights = nights

        else: #게임이 아직 끝나지 않았다면
            if n % 2: #day
                max_guilt = max(guilt)
                idx = guilt.index(max_guilt)
                guilt[idx] = 0
                play(nights, n-1)
                if flag==0:return
                guilt[idx] = max_guilt

            else: #night
                for idx in range(N): #죽을 사람 정하기
                    night_temp = guilt[idx]
                    if idx == mafia or guilt[idx]==0: #마피아거나 죽은사람이면 패스
                        continue
                    for j in range(N): #다른사람
                        if guilt[j]: #안죽었다면
                            guilt[j] += R[idx][j] #유죄지수 변경
                    guilt[idx] = 0
                    play(nights+1, n-1)
                    if flag==0: return
                    for j in range(N):
                        if guilt[j]:
                            guilt[j] -= R[idx][j]
                    guilt[idx] = night_temp


N = int(input())
guilt = list(map(int, input().split()))
R = [list(map(int, input().split())) for _ in range(N)]
mafia = int(input())

nights = 0
max_nights = 0


flag = 1
play(nights, N)
print(max_nights)
