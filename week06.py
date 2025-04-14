class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        self.size = self.size + 1
        node = Node(data)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.link = node
            self.rear = node    # move


    def dequeue(self):    # dequeue - 빼기
        if self.front is None:  # q의 front 값이 none
            raise IndexError("Queue is empty!") # q 비어있다
        self.size = self.size - 1   # 1개 삭제
        temp = self.front
        self.front = self.front.link    # move
        if self.front is None:
            self.rear = None
        return temp.data

q = Queue()
q.enqueue("Data structure")     # front
q.enqueue("Database")
print(q.size, q.front.data, q.rear.data)
print(q.dequeue())
print(q.size, q.front.data, q.rear.data)
print(q.dequeue())