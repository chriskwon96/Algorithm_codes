from itertools import combinations

N, K = map(int, input().split())
# 0 < N <= 50 , 0 <= K <= 26

# anta로 시작, tica로 끝난다
# antic 는 무조건 있어야 해

must_have = {"a", "n", "t", "i", "c"}


if K < 5:
    print(0)
elif K == 26:
    print(N)
else:
    max_ans = 0
    cur_ans = 0
    min_ans = 0
    words = []
    leftovers = set()
    # words = list(set(input()).difference(must_have) for _ in range(N))
    for _ in range(N):
        word = set(input())-must_have
        if len(word) == 0:
            min_ans += 1
        elif len(word) <= K-5:
            words.append(word)
            leftovers = leftovers | word

    for comb in combinations(list(leftovers), K-5):
        cur_ans = min_ans
        for word in words:
            # print(word)
            if word.issubset(set(comb)) :
                cur_ans += 1
        if cur_ans > max_ans:
            max_ans = cur_ans
    print(max_ans)





