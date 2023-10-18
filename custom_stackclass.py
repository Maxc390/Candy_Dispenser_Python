# Stack variables using a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top_node = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        if self.top_node:
            new_node.next = self.top_node
        self.top_node = new_node
        self.size += 1

    def pop(self):
        if not self.is_empty():
            popped_item = self.top_node.data
            self.top_node = self.top_node.next
            self.size -= 1
            return popped_item
        return None

    def peek(self):
        return self.top_node.data if self.top_node else None

    def is_empty(self):
        return self.size == 0

    def length(self):
        return self.size
