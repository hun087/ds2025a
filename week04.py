import random


class Node:
    def __init__(self, data, links=None):
        self.data = data
        self.link = links

# a = None("ABC")
class LinkedList:
    def __init__(self):
        self.head = None    #false


    def append(self, data):
        if not self.head:       # if~return 1번만
            self.head = Node(data)  #data -> 8
            return
        current = self.head     # current - 지역변수
        while current.link:
            current = current.link
        current.link = Node(data)


    #def is_find(self, target):    # is - 명제
    def search(self, target):
        current = self.head
        while current.link:
            if target == current.data:
                return f"{target}을(를) 찾았습니다!"
            else:
                current = current.link
        return f"{target}은(는) 링크드 리스트 안에 존재하지 않습니다."



    def __str__(self):
        current = self.head
        result = ""
        while current is not None:
            # result = result + str(current.data) + " -> "
            result = result + f"{current.data} -> "
            current = current.link
        return result + "END"

ll = LinkedList()
for _ in range(20):
    ll.append(random.randint(1, 30))
print(ll)
print(ll.search(10))

#ll = LinkedList()
#ll.append(8)
#ll.append(10)
#ll.append(-9)
#print(ll)
#print(ll.is_find(99))
#print(ll.is_find(10))
#print(ll.search(99))
#print(ll.search(10))
