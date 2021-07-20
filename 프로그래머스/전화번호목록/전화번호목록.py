

def solution(phone_book):
    N = len(phone_book)
    phone_book.sort(key= lambda x:len(x))
    for i in range(N-1):
        for j in range(i+1, N):
            n = len(phone_book[i])
            if phone_book[i] == phone_book[j][:n]:
                return False
    return True

print(solution(["123","456","789"]))
