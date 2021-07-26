

def divide_multiply(n, times):
    if times == 1:
        return n
    else:
        if times %2 == 0: #even num
            return divide_multiply(n, times // 2) ** 2
        else:
            return divide_multiply(n, times//2) **2 * n

A, B, C = map(int, input().split())

