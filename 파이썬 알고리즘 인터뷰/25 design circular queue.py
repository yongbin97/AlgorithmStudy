class MyCircularQueue:
    def __init__(self, k: int):
        self._queue = [None] * k
        self._size = k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self._queue[self.rear] is not None:
            return False

        else:
            self._queue[self.rear] = value
            self.rear = (self.rear + 1) % self._size
            return True

    def deQueue(self) -> bool:
        if self._queue[self.front] is None:
            return False
        else:
            self._queue[self.front] = None
            self.front = (self.front + 1) % self._size
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self._queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            rear_pointer = self._size - 1 if self.rear == 0 else self.rear - 1
            return self._queue[rear_pointer]

    def isEmpty(self) -> bool:
        return all(e is None for e in self._queue)

    def isFull(self) -> bool:
        return None not in self._queue
