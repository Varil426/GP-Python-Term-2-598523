class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        # TODO
        pass

    def enqueue(self, item):
        # TODO
        pass

    def dequeue(self):
        # TODO
        pass

    def peek(self):
        # TODO
        pass


# Testy
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # 1
print(queue.dequeue())  # 2
print(queue.is_empty())  # False
print(queue.dequeue())  # 3
print(queue.is_empty())  # True
