






def solution(n, times):
    left, right = 1, max(times) * n
    ans = 0

    while left <= right:
        mid = (left+right) // 2
        people = 0
        for i in times:
            people += mid // i
            if people >= n:
                break
        if people >= n:
            ans = mid
            right = mid - 1

        elif people < n:
            left = mid + 1
    return ans