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

    def __str__(self):
        current = self.head
        result = ""
        while current is not None:
            # print(current.data)
            result = result + str(current.data) + " -> "
            current = current.link
        return result + "END"
        #return "Linked list!"

ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)
print(ll)

