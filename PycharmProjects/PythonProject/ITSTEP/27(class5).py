# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#     def __str__(self) -> str:
#         return str(self.data)
#
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
#
# node1.next = node2
# node2.next = node3
# print(node1.next)
# print(node2.next)
#
# print(node1.next.next.data)



# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#     def count(self):
#         total = 0
#         current = self
#         while current:
#             total += 1
#             current = current.next
#         return total
#
# node1 = Node("Python")
# node2 = Node("Java")
# node3 = Node("C++")
# node1.next = node2
# node2.next = node3
# current = node1
#
# while current:
#     print(current.value, end=" -> ")
#     current = current.next
# print("None")
# print(f"Total nodes: {node1.count()}")






class Node:
    def __init__(self, title):
        self.title = title
        self.next = None
        self.prev = None

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, title):
        new_node = Node(title)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
    def show_forward(self):
        current = self.head
        while current:
            print(current.title)
            current = current.next
    def show_backward(self):
        current = self.tail
        while current:
            print(current.title)
            current = current.prev

playlist = Playlist()
playlist.append("Bohemian Rhapsody")
playlist.append("Believer")
playlist.append("Numb")
playlist.append("Take On Me")
print("Forward:")
playlist.show_forward()
print("\nBackward:")
playlist.show_backward()