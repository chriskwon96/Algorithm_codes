def perm(x, n, k):
    global cnt, ans, flag
    if flag:
        if x == n :
            if cnt == k:
                ans = p[:]
                flag = 0
                return
            cnt += 1

        else:
            for i in range(n):
                # print(v)
                if v[i] == 0:
                    v[i] = 1
                    p[x] = A[i]
                    perm(x+1, n, k)
                    v[i] = 0
    return


def solution(n,k):
    global v,p,A,cnt,cand,flag
    v = [0] * n
    p = [0] * n
    A = list(range(1, n + 1))
    cnt = 1
    cand = []
    flag = 1
    perm(0, n, k)
    return ans


print(solution(3,5))

