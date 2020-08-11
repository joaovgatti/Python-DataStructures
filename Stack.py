class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class Stack:

    def __init__(self):
        self.head = None

    def push(self, v):
        temp = Node(v)
        if self.head is None:
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp

    def pop(self):
        self.head = self.head.next

    def printStack(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(123)
    stack.push(90)
    stack.push(223)
    stack.push(1923)
    stack.printStack()
    stack.pop()
    stack.pop()
    stack.printStack()
