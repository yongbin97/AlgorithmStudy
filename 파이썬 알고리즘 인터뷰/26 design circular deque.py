from collections import deque

class MyCircularDeque:
    def __init__(self, k: int):
        self._size = k
        self._queue = deque(maxlen=k)

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self._queue.appendleft(value)
            return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self._queue.append(value)
            return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self._queue.popleft()
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self._queue.pop()
            return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self._queue[0]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self._queue[-1]

    def isEmpty(self) -> bool:
        if len(self._queue) == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if len(self._queue) >= self._size:
            return True
        else:
            return False

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()