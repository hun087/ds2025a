import random


class Node:
    def __init__(self, data, link=None):
        self.data = data


@ @-9

, 14 + 11, 25 @ @


def __init__(self):
    self.head = None


def append(self, data):
    if not self.head:  # 링크드리스트가 노드가 하나도 없는 상태면
        self.head = Node(data)  # 새 노드를 head에 연결
    if not self.head:
        self.head = Node(data)
        return
    current = self.head
    while current.link:
        current = current.link  # 다음노드로 이동
        current = current.link
    current.link = Node(data)


def search(self, target):
    current = self.head
    while current.link:
        if current.data == target:
            return f"{target}을(를) 찾았습니다"
        else:
            current = current.link
    return f"{target}은(는) 링크드리스트 안에 존재하지 않습니다"


def __str__(self):
    node = self.head
    out_texts = ""


@ @-26

, 8 + 39, 17 @ @


def __str__(self):
    return out_texts + "end"


# ll = LinkedList()
# ll.append(8)
# ll.append(10)
# ll.append(-9)
# print(ll)
# print(ll.search(100))
# print(ll.search(10))

ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)
for _ in range(10):
    ll.append(random.randint(1, 30))

print(ll)
print(ll.search(10))