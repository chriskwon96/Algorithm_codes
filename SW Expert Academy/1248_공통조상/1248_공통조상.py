def FindParent(node):
    global parents
    if p[node] != 0: # 부모 노드가 있다면
        parents.append(p[node])
        FindParent(p[node])

def FindChild(node):
    global child
    for i in range(V+1):
        if p[i] == node:
            child.append(i)
            FindChild(i)

T = int(input())
for t in range(1, T+1):
    V, E, n1, n2 = map(int, input().split())
    edges = list(map(int, input().split()))
    p = [0]*(V+1)
    for i in range(E):
        p[edges[2*i+1]] = edges[2*i]

    parent_list = []
    for i in [n1,n2]:
        parents = []
        FindParent(i)
        parent_list.append(parents)

    for i in parent_list[0]:
        if i in parent_list[1]:
            break

    child = []
    FindChild(i)

    print('#{} {} {}'.format(t, i, len(child)+1))

