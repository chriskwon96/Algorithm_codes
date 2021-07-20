

def solution(n):
    ans = ""
    while n//3:
        de, re = divmod(n,3)
        if re == 0:
            re = 4
            de -= 1
        ans = str(re) + ans
        n = de
        # print(de, re)
    if n == 0:
        return ans
    else:
        return str(n) + ans


print(solution(4))







