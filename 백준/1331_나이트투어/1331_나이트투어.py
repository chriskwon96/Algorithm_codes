
def knight_move(si, sj,target):
    possibles = [(si+1, sj+2),(si-1, sj+2),(si+2, sj+1),(si+2,sj-1),(si+1, sj-2),(si-1, sj-2),(si-2, sj+1),(si-2,sj-1)]
    if target in possibles:
        return "Valid"
    return "Invalid"


moves = [input() for _ in range(36)]

# 중복이 없는가
if len(set(moves)) < 36:
    result = "Invalid"

else:
    moves = list(map(lambda ele:(ord(ele[0])-ord("A"),int(ele[1])-1), moves))

    for k in range(36): #knight로 이동 가능한가
        if k < 35:
            result = knight_move(moves[k][0],moves[k][1], moves[k+1])
        else: #원점으로 돌아올 수 있는가
            result = knight_move(moves[k][0], moves[k][1], moves[0])

        if result == "Invalid":
            break

print(result)




