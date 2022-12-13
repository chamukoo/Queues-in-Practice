# Queues: Firs-In, First-Out (FIFO)

from collections import deque
from heapq import heappop, heappush
from itertools import count

# Initializing Class: Queue
class Queue:
    def __init__(self, *elements):
        self._elements = deque(elements)

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()
 
    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()


# Initializing Class: Stack(Queue)
class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()


# Initializing Class: Priority Queue
class PriorityQueue:
    def __init__(self):
        self._elements = []

    def enqueue_with_priority(self, priority, value):
        # heappush(self._elements, (priority, value))

        # Making the priority a negative number so that 
        # the highest one becomes the lowest
        heappush(self._elements, (-priority, value))


    def dequeue(self):
        # return heappop(self._elements)
        return heappop(self._elements)[1]


# Initializing Class: Priority
class PriorityQueue:
    def __init__(self):
        self._elements = []
        self._counter = count()

    def enqueue_with_priority(self, priority, value):
        element = (-priority, next(self._counter), value)
        heappush(self._elements, element)

    def dequeue(self):
        return heappop(self._elements)[-1]


# Initializing Class: Interable Misin
class IterableMixin:
    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

            