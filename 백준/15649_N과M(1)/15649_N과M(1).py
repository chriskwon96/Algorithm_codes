import sys


N, M = map(int, sys.stdin.readline().split())
my_list = list(range(1, N+1)) #나의 숫자 list
check = [0]*N # 이 원소가 사용되었나 확인
final_arr = [0]*M # 수열

def perm(cnt):
    if cnt == M: #목표 개수에 도달하면
        print(*final_arr)
    else:
        for i in range(N): #범위전체
            if check[i] == 0: #사용되지 않았으면
                check[i] = 1 #사용하고
                final_arr[cnt] = my_list[i]
                perm(cnt+1) #다음 위치의 원소를 결정하자
                check[i] = 0 # 리셋

perm(0)



