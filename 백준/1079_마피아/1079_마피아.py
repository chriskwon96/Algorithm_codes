

def play(nights, n):
    global max_nights, flag

    if flag:
        if guilt[mafia] == 0 or n == 1 : #마피아가 죽었다면 아니면 마피아 빼고 다죽었다면
            if n==1: #마피아가 승리한 경우 == 최고
                flag = 0
            if nights > max_nights:
                max_nights = nights
                # print(max_nights)
        else: #게임이 아직 끝나지 않았다면

            if n % 2: #day
                max_guilt = max(guilt)
                # print("++++", nights, n, guilt, max(guilt))
                for idx in range(N):
                    # print(guilt[idx])
                    if guilt[idx] == max_guilt:
                        guilt[idx] = 0
                        # print("====", idx, guilt)
                        play(nights, n-1)
                        if flag==0:return
                        guilt[idx] = max_guilt

                        break
            else: #night
                for idx in range(N):
                    night_temp = guilt[idx]
                    if guilt[idx] != 0 and idx != mafia:
                        for j in range(N):
                            if guilt[j] != 0:
                                guilt[j] += R[idx][j]
                        guilt[idx] = 0

                        play(nights+1, n-1)
                        if flag==0: return

                        for j in range(N):
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







