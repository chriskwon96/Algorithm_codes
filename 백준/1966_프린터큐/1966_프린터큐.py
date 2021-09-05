

tc = int(input())

for t in range(tc):
    N, M = map(int, input().split())
    priority_list = list(map(int, input().split()))
    index_list = list(range(N))
    order = 1

    while True:
        top_priority = max(priority_list)

        if priority_list[0] == top_priority:
            if index_list[0] == M:
                print(order)
                break
            else:
                priority_list.pop(0)
                index_list.pop(0)
                order += 1

        else:
            priority_list.append(priority_list.pop(0))
            index_list.append(index_list.pop(0))









