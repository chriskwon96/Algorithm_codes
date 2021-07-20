
N = int(input())
reserve = [list(map(int, input().split())) for _ in range(N)]
ans = []
reserve.sort(key=lambda x:x[0])
reserve.sort(key=lambda x:x[1])

start_time = 0
cnt = 0
for re in reserve:
    if start_time <=re[0]:
        cnt += 1
        start_time = re[1]
print(cnt)












