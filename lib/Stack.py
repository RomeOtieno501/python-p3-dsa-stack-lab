class Stack:
    def __init__(self, items=None, limit=100):
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise OverflowError("Stack is full")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise IndexError("Peek from empty stack")

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        try:
            return len(self.items) - 1 - self.items[::-1].index(target)
        except ValueError:
            return -1
