
T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    store = [0] * N
    
    my_board = [list(map(int, input().split())) for _ in range(N)]


    more_stores = []
    for row in my_board:
        stores = []
        store = 0
        for i in row:
            if i == 0:
                store = 0
            else:
                store += 1
            stores.append(store)
        
        more_stores.append(stores)
    #print(more_stores)


    more_stores_col = []
    for i in range(N):
        store = 0
        stores_col = []
        for j in range(N):                     
            if my_board[j][i] == 0:
                store = 0
            else:
                store += 1

            stores_col.append(store)
        more_stores_col.append(stores_col)
    

    cnt = 0   
    for i in range(N):
        for j in range(N-1):
            if (more_stores[i][j] == K) and (more_stores[i][j+1] == 0):
                cnt += 1

            if (more_stores_col[i][j] == K) and (more_stores_col[i][j+1] == 0):
                cnt+=1

        j =N-1
        if more_stores[i][j] == K:
            cnt+=1
        if more_stores_col[i][j]== K:
            cnt +=1

                    
    print('#{} {}'.format(t,cnt))



