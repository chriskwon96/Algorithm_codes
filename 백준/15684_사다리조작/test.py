

N, M, H = map(int, input().split())
Hs = {}
goal = list(range(1, N+1))
for i in range(1, H+1):
    Hs[i] = []

# print(Hs)
for _ in range(M):
    a, b = map(int, input().split())
    Hs[a].append(b)
# print(Hs)
ans = -1
cnt = 0
flag = 0

def f(Hs, cnt, pos, Hidx): #사다리타기
    # print(Hs)
    global flag
    if cnt <= 3:
        #사다리타기
        pos = list(range(1, N+1))
        for i in range(1, H+1): #매층마다
            if Hs[i]:
                for j in Hs[i]:
                    pos[j-1], pos[j] = pos[j], pos[j-1] #swap
        # print("사다리결과:", pos)
        # print(goal, pos)
        if goal == pos: #사다리타기 성공이면
            flag = 1
            print(cnt)
        else: #아니라면
            #길 추가해주고 다시 f()
            for x in range(1, H+1):
                for y in range(1, N):
                    if y not in Hs[x] and y+1 not in Hs[x] and y-1 not in Hs[x]:
                        Hs[x].append(y)
                        f(Hs, cnt+1, )
                        Hs[x].pop()
                    if flag:
                        break
                if flag:
                    break

f(Hs, cnt)
if not flag:
    print(ans)
# print(result)

