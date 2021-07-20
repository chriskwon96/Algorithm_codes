# 단일(단순) 연결 리스트
class Node:
    def __init__(self, d=0, n=None):
        self.data = d  # 정수 값
        self.next = n  # 다음 노드 주소


class LinkedList:
    def __init__(self):
        self.head = None  # 첫 번째 노드
        self.tail = None  # 마지막 노드
        self.size = 0  # 노드의 수


mylist = LinkedList()


def printList(lst):  # lst: LinkedList객체, 디버그용도로 쓸 수 있다
    if lst.head is None: return  # 빈 리스트 일 경우

    cur = lst.head
    print(lst.size, '[', end=' ')

    while cur is not None:
        print(cur.data, end=' ')
        cur = cur.next
        # while cur.next 일 경우 끝나고 cur는 마지막노드
    print(']')


def insertLast(lst, new):  # new: 새로 추가할 노드 객체
    # 빈 리스트일 경우
    if lst.head is None:
        lst.head = lst.tail = new
    # else: # tail추가 했으므로 필요없음
    #     # 마지막 노드를 찾는다.
    #     cur = lst.head
    #     while cur.next is not None:
    #         cur = cur.next
    #     cur.next = new
    else:
        lst.tail.next = new
        lst.tail = new
    lst.size += 1


def deleteLast(lst):
    if lst.head is None: return

    pre, cur = None, lst.head  # pre => 이전 노드
    while cur.next is not None:
        pre = cur
        cur = cur.next
    if pre is None:  # 원소가 하나일 때
        lst.head = lst.tail = None
    else:
        pre.next = None
        lst.tail = pre
    lst.size -= 1


def insertFirst(lst, new):
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        new.next = lst.head
        lst.head = new
    lst.size += 1


def deleteFirst(lst):
    if lst.head is None: return

    # 노드가 1개일 경우 주의한다.
    lst.head = lst.head.next
    if lst.head is None:
        lst.tail = None
    lst.size -= 1


def insertAt(lst, idx, new):  # 임의의 위치 idx: 인덱스값
    # 빈리스트일 경우, idx == 0
    if lst.head is None or idx == 0:
        insertFirst(lst, new)
    elif idx >= lst.size:  # 마지막 추가하는 경우 idx >= lst.size
        insertLast(lst, new)
    else:
        # 중간에 추가하는 경우
        pre, cur = None, lst.head
        for _ in range(idx):
            pre = cur
            cur = cur.next

        new.next = cur
        pre.next = new
        lst.size += 1


def deleteAt(lst, idx):
    if idx == 0:
        deleteFirst(lst)
    elif idx == lst.size:
        deleteLast(lst)
    elif idx > lst.size:
        pass
    else:
        pre, cur = None, lst.head
        for _ in range(idx):
            pre = cur
            cur = cur.next
        pre.next = cur.next
        lst.size -= 1




T = int(input())

for t in range(1, T+1):
    mylist = LinkedList()
    N, M, L = map(int, input().split())
    num = list(map(int, input().split()))
    for i in range(N):
        insertLast(mylist, Node(num[i]))
    for _ in range(M):
        move = list(map(str, input().split()))
        command = move[0]
        if command == "I":
            insertAt(mylist, int(move[1]), Node(int(move[2])))
        elif command == "D":
            deleteAt(mylist, int(move[1]))
        else:
            cur = mylist.head
            for _ in range(int(move[1])):
                cur = cur.next
            cur.data = int(move[2])

    print("#{}".format(t), end =" ")
    cur = mylist.head
    if mylist.size >= L:
        for _ in range(L):
            cur = cur.next
        print(cur.data)
    else:
        print(-1)
