from queue import Queue     # 클래스 설계 필요x

q = Queue()
q.put("Data structure")
q.put("Database")
q.put("Javascript")
print(q.qsize())
print(q.get())  #dequeue
print(q.qsize())
print(q.get())
print(q.qsize())
print(q.get())
print(q.qsize())