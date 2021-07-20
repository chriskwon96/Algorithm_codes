from math import ceil

def solution(people, limit):
    N = len(people)
    people.sort(reverse=True)
    ans = N
    j = N-1
    for i in range(N):
        if i==j: break
        elif people[i] + people[j] <= limit:
            ans -= 1
            j -= 1
            if i == j:
                break

    return ans

print(solution([70, 50, 80, 50]	, 100))
print(solution([70, 80, 50], 100))
print(solution([50,50,50,50,40,60], 100))
print(solution([30,80,80,80], 100))
print(solution([20, 50, 50, 80], 100))
print(solution([1,1,1,1], 100))
print(solution([1],100))
print(solution([1,1,30],100))
print(solution([10,10,10],5))
print(solution([100,100], 100))
print(solution([10, 50, 55, 90], 100))




