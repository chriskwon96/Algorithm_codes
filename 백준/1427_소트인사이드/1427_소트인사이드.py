N = list(map(int, input()))
# N.sort(reverse=True)
# print(''.join(map(str, N)))
for j in range(len(N)-1, -1, -1):
    for i in range(j):
        if N[i] < N[i+1]:
             N[i], N[i+1] = N[i+1], N[i]

for i in N:
    print(i, end = '')
