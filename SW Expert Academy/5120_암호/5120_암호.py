class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d  # 정수 값
        self.prev = p
        self.next = n  # 다음 노드 주소


class LinkedList:
    def __init__(self):
        self.head = None  # 첫 번째 노드
        #self.tail = None  # 마지막 노드
        self.size = 0  # 노드의 수


def printList(lst):  # lst: LinkedList객체, 디버그용도로 쓸 수 있다
    if lst.head is None: return  # 빈 리스트 일 경우
    cur = lst.head
    if lst.size < 10:
        for _ in range(lst.size):
            cur = cur.prev
            print(cur.data, end=' ')
    else:
        for _ in range(10):
            cur = cur.prev
            print(cur.data, end=' ')

    print()



def insertLast(lst, new):  # new: 새로 추가할 노드 객체
    # 빈 리스트일 경우
    if lst.head is None:
        lst.head = new
        new.prev = new.next = new
    else:
        tail = lst.head.prev
        new.prev = tail
        new.next = lst.head
        tail.next = new
        lst.head.prev = new

    lst.size += 1


T = int(input())
for t in range(1, T+1):
    mylist = LinkedList()
    N, M, K = map(int, input().split())
    nums = list(map(int, input().split()))
    for i in range(N):
        insertLast(mylist, Node(nums[i]))
    cur = mylist.head

    for k in range(K):
        for _ in range(M):
            cur = cur.next
        new = Node(cur.data+cur.prev.data)
        cur.prev.next = new
        new.prev = cur.prev
        new.next = cur
        cur.prev = new

        cur = new
        mylist.size += 1
    print("#{} ".format(t), end="")
    printList(mylist)
