def solution(n,s): #n: 자연수의 개수 #s: 자연수의 합
    if n > s:
        return [-1]
    else:
        A = [0]*n
        for i in range(n):
            A[i] = s//n
        s -= n*(s//n)

        i = 0
        while s:
            A[i] += 1
            s -= 1
            i += 1
        return sorted(A)


print(solution(2,1))