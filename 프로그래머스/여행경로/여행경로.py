

def f(end, tickets, q):
    global flag, ans
    # print(end, q, tickets)
    if flag: return
    else:
        if tickets:
            for ticket in tickets:
                if ticket[0] == end:
                    tickets.remove(ticket)
                    q.append(ticket[1])
                    f(ticket[1], tickets , q)
                    if flag: return
                    tickets.insert(0, ticket)
                    q.pop()
        else:
            flag = 1
            ans = q
            return


def solution(tickets):
    global flag, ans
    tickets.sort(key=lambda x:x[1]) # 도착지 기준으로 소팅
    end = "ICN"
    q = ["ICN"]
    ans = ""
    flag = 0
    f(end, tickets, q)
    return ans


# solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))








