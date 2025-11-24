class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        # TODO
        pass

    def pop(self):
        # TODO
        pass

    def peek(self):
        # TODO
        pass

    def is_empty(self):
        # TODO
        pass

    def size(self):
        # TODO
        pass


# Testy
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # 3
print(stack.peek())  # 2
print(stack.is_empty())  # False
print(stack.size())  # 2
