import datetime
import numpy as np


class QueueCircleList:
    """
    Implementation of Circle Queue with Dynamic Array (list)
    """
    def __init__(self, n: int):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.size += 1
            self.tail = (self.tail + 1) % self.max_n

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.size -= 1
        self.head = (self.head + 1) % self.max_n
        return x


class QueueCircleArray:
    """
    Implementation of Circle Queue with Numpy Array.
    """
    def __init__(self, n: int):
        self.queue = np.full(n, fill_value=np.NaN)
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.size += 1
            self.tail = (self.tail + 1) % self.max_n

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = np.NaN
        self.size -= 1
        self.head = (self.head + 1) % self.max_n
        return x


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class QueueCircleLinked:
    """
    Implementation of Circle Queue with Linked List.
    """
    def __init__(self, n: int):
        first_node = new_node = Node()
        for _ in range(n - 1):
            new_node = Node(next_node=new_node)
        first_node.next_node = new_node
        self.max_n = n
        self.size = 0
        self.tail = first_node
        self.head = first_node

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_n

    def push(self, x):
        if self.is_full():
            return Exception("The queue is full. You cannot push to full queue.")
        self.head.data = x
        self.head = self.head.next_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return Exception("The queue is empty. You cannot pop from empty queue.")
        deleted = self.tail.data
        self.tail.data = None
        self.tail = self.tail.next_node
        self.size -= 1
        return deleted


if __name__ == "__main__":
    ds_1 = QueueCircleList(1000000)
    start_1 = datetime.datetime.now()
    for _ in range(1000000):
        ds_1.push(3)
        ds_1.pop()
    finish_1 = datetime.datetime.now()
    print("Время, требующееся циклической очереди на list для выполнения"
          " по 1 000 000 операций вставки и удаления: {}".format(finish_1-start_1))

    ds_2 = QueueCircleArray(1000000)
    start_2 = datetime.datetime.now()
    for _ in range(1000000):
        ds_2.push(3)
        ds_2.pop()
    finish_2 = datetime.datetime.now()
    print("Время, требующееся циклической очереди на array для выполнения"
          " по 1 000 000 операций вставки и удаления: {}".format(finish_2-start_2))

    ds_3 = QueueCircleLinked(1000000)
    start_3 = datetime.datetime.now()
    for _ in range(1000000):
        ds_3.push(3)
        ds_3.pop()
    finish_3 = datetime.datetime.now()
    print("Время, требующееся циклической очереди на linked list для выполнения"
          " по 1 000 000 операций вставки и удаления: {}".format(finish_3-start_3))
