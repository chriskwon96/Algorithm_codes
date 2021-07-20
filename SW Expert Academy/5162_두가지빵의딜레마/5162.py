T = int(input())
for t in range(1, T+1):
    A, B, C = map(int, input().split())
    bread = C // min(A,B)
    print("#{} {}".format(t, bread))