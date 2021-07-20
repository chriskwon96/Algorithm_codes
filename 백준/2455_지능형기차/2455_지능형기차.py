train = []
for _ in range(4):
    off, on = map(int, input().split())
    train.append([-off, on])

for i in range(4):
    if i == 0:
        train[i] = sum(train[i])
    else:
        train[i] = sum(train[i]) + train[i-1]
print(max(train))
