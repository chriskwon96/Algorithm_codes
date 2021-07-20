
def solution(A, B):
    B.sort(reverse=True)
    A.sort(reverse=True)
    points = 0

    for b in B:
        for a in A:
            if b > a:
                points += 1
                A.remove(a)
                break
        if A:
            if a == A[-1]:
                break

    return points






# A = [5,1,3,7]
# B = [2,2,6,8]

A=[2,2,2,2]
B=[1,1,1,1]



print(solution(A,B))





