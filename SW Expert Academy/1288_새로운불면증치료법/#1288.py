# N = input()

num_times=int(input()) # number of times of input
attempts = 1

while attempts <= num_times:
    cnt = 0  # num of attempts
    N = input()
    saw = set()
    final = set(range(10))  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

    n_times_N = N
    # check final vs saw
    while saw != final:

        for i in set(n_times_N):

            i = int(i)
            saw.add(i)

        cnt += 1
        n_times_N = str(cnt * int(N))


    print('#{} {}'.format(attempts, (cnt-1)*int(N)))
    attempts += 1





