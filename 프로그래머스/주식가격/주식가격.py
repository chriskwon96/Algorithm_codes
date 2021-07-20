def solution(prices):
    N = len(prices)
    ans = []
    for i in range(N-1):
        flag = 1
        for j in range(i+1, N):
            if prices[i] > prices[j]:
                ans.append(j-i)
                flag = 0
                break
        if flag: ans.append(N-1-i)
    ans.append(0)

    return ans


print(solution([1, 2, 3, 2, 3]))
