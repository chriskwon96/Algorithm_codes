# id 길이는 3이상 15이하
# 알파벳 소문자, 숫자, - , _, . 사용
# .는 처음 끝 안됨, 연속 안됨



def solution(new_id):
    # step 1
    new_id = new_id.lower()

    # step 2
    new_id_2 = []
    for ch in new_id:
        if ch.isalpha() or ch.isdigit() or ch in ["-", "_", "."]:
            new_id_2.append(ch)

    # step3
    i = 0
    N = len(new_id_2)
    while i < N-1 :
        if new_id_2[i] == "." == new_id_2[i+1]:
            new_id_2.pop(i)
            N -= 1
            continue
        i += 1

    # step 4
    if new_id_2 and new_id_2[0] == ".":
        new_id_2.pop(0)
    if new_id_2 and new_id_2[-1] == ".":
        new_id_2.pop()

    # step 5
    if len(new_id_2) == 0:
        new_id_2.append("a")
    # print(new_id_2)

    #step 6
    if len(new_id_2) >= 16:
        new_id_2 = new_id_2[:15]
        if new_id_2[-1] == ".":
            new_id_2.pop()

    # step 7
    while len(new_id_2) < 3:
        new_id_2.append(new_id_2[-1])

    return "".join(new_id_2)





print(solution(input()))


