# info 1 <= <=50000
# cpp / java / python
# backend / frontend
# junior / senior
# chicken / pizza
# coding test score 1<= <=100000
# space
# query 1<= <=100000
# [requirements ] score , score <=
def solution(info, query):
    app_info = []

    for people in info:
        app_info.append(people.split())
    # print(app_info)
    result = []

    for q in query:
        ans = 0
        N = len(info)
        app_index = list(range(N))

        # print(app_index, N)
        q_split = q.split()
        # filtering
        for i in range(0, 4): # check requirement

            if q_split[2*i] == "-" : continue
            idx = 0
            while idx < N:
                # print(app_index[idx])
                if app_info[app_index[idx]][i] != q_split[2*i]:
                    app_index.pop(idx)
                    N -= 1
                    continue
                idx += 1
        # print(app_index)
        for idx in app_index:
            if int(app_info[idx][4]) >= int(q_split[7]):
                ans += 1
        result.append(ans)
    return result











info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))


