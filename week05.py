class Stack:
    def __init__(self):
        self.items = list()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0 # == 0 true

    def peek(self):     # 삭제기능 x 확인
        return self.items[-1]


s1 = Stack()
s2 = Stack()
print(s1.is_empty())    #True
s1.push("Data structure")
print(s1.is_empty())    #False
print(s2.is_empty())    #True
s1.push("Database")
print(s1.size())        #2
print(s1.peek())        #DB
print(s1.size())        #2
print(s1.pop())         #DB
print(s1.size())        #1
print(s1.peek())        #DS