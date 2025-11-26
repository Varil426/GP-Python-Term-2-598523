class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            # return self.stack.pop()
            last_element = self.stack[-1]
            self.stack = self.stack[0:-1]
            return last_element

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.stack)


# Testy
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # 3
print(stack.peek())  # 2
print(stack.is_empty())  # False
print(stack.size())  # 2
