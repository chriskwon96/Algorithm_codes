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
    N = len(info)
    for people in info:
        app_info.append(people.split())

    result = []

    for q in query:
        ans = 0
        app_index = list(range(N))

        q_split = q.split()
        # filtering
        for i in range(4): # check requirement
            new_idx = []
            if q_split[2*i] == "-" : continue
            for idx in app_index: #idx번째 지원자의 i번째 조건이 충족된다면
                if app_info[idx][i] == q_split[2*i]:
                    new_idx.append(idx)
            app_index = new_idx

        # check score
        for idx in app_index:
            if int(app_info[idx][4]) >= int(q_split[7]):
                ans += 1
        result.append(ans)

    return result






info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))


