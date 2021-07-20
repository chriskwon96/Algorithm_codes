class Node:
    def __init__(self, d=0, n=None):
        self.data = d # 정수값
        self.next = n # 다음 노드 주소

class LinkedList:
    def __init__(self):
        self.head = None # 첫 번째 노드
        self.tail = None # 마지막 노드
        self.size = 0 # 노드의 수

def printList(lst):
    if lst.head is None: return

    cur = lst.head
    print(lst.size, '[', end= ' ')

    while cur is not None:
        print(cur.data, end=' ')
        cur = cur.next
    print(']')

def insertLast(lst, new):
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        lst.tail.next = new
        lst.tail = new
    lst.size += 1


def insertFirst(lst, new):
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        new.next = lst.head
        lst.head = new
    lst.size += 1


def insertAt(lst, idx, new):
    if lst.head is None or idx == 0 :
        insertFirst(lst, new)
    elif idx >= lst.size:
        insertLast(lst, new)
    else:
        pre, cur = None, lst.head
        for _ in range(idx):
            pre = cur
            cur = cur.next
        new.next = cur
        pre.next = new
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


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    mylist = LinkedList()
    nums = list(map(int, input().split()))
    for i in range(N):
        insertLast(mylist, Node(nums[i]))

    for _ in range(M-1):
        nums = list(map(int, input().split()))
        flag = 0
        cur = mylist.head
        while cur:
            if nums[0] < cur.data:
                for k in range(N-1, -1, -1):
                    insertAt(mylist, flag, Node(nums[k]))
                break
            else:
                cur = cur.next
                flag += 1
        if not cur:
            for k in range(N):
                insertLast(mylist,Node(nums[k]))

    print("#{}".format(t), end=" ")
    for _ in range(10):
        print(mylist.tail.data, end =' ')
        deleteLast(mylist)
    print()










