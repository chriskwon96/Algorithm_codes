def dfs(n, idx):
    global max_ans
    if n == K-5:
        cur_ans = 0
        for word in words:
            for w in word:
                if check[ord(w)-ord("a")] == 0:
                    break
            else:
                cur_ans += 1

        max_ans = max(max_ans, cur_ans)
    else:
        for i in range(idx, 26):
            if check[i] == 0:
                check[i] = 1
                dfs(n+1, i)
                check[i] = 0


N, K = map(int, input().split())

must_have = {"a", "n", "t", "i", "c"}

max_ans = 0

if K < 5:
    print(0)
elif K == 26:
    print(N)
else:
    words = list(set(input()[4:-4])-must_have for _ in range(N))
    check = [0] * 26

    for ch in must_have:
        check[ord(ch)-ord("a")] = 1
    dfs(0,0)
    print(max_ans)

