# 격자의 상태가 담긴 2차원 배열 board
# 크레인을 작동시킨 위치가 담긴 배열 moves
# 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return
def getTopDoll(board, pos):
    for i in range(N):
        if board[i][pos] != 0: #i가장 빨리 인형을 찾으면
            doll = board[i][pos] # 인형겟
            board[i][pos] = 0 # 인형 빼줘
            return doll #인형의 종류(숫자)를 리턴

def check(basket, doll): #인형이랑 바구니 가장 윗놈이랑 검사
    if basket[-1] == doll: #같은 인형이라면
        return True #지워줘
    else:
        return False #냅둬


def solution(board, moves):
    global N
    N = len(board)
    basket = []
    cnt = 0
    for move in moves:
        # print(basket)
        doll = getTopDoll(board, move-1) # 가장 위에 있는 인형 잡기
        if doll: #인형이 있을 때만 동작
            if basket: #바구니에 인형이 존재한다면
                if check(basket, doll):
                    basket.pop() #바구니 가장 윗놈 지우기
                    cnt += 2
                else:
                    basket.append(doll)  # 인형을 바구니에 추가
            else:
                basket.append(doll)  # 인형을 바구니에 추가
    return cnt





board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))


