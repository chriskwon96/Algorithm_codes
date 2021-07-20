def f(n,k,v,my_list):
    global max_num
    if n == k :
        if int("".join(my_list)) > max_num:
            max_num = int("".join(my_list))
            print(max_num)
    else:
        for i in range(n+1, N):
            if v[i] == 0:
                v[i] = 1
                temp = my_list[i]
                my_list[i] = ""
                f(n+1, k, v, my_list)
                my_list[i] = temp
                v[i] = 0



def solution(number,k):
    global N, max_num
    N = len(number)
    max_num = 0
    v = [0] * N
    for n in range(N-k):
        f(n, k, v, list(number))
    return max_num

print(solution("1924", 2))

