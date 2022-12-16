# queues.py

from dataclasses import dataclass
from collections import deque
from heapq import heappop, heappush, heapify
from itertools import count
from typing import Any

# Initializing Class: Interable Misin
class IterableMixin:
    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()


# Initializing Class: Queue
class Queue(IterableMixin):
    def __init__(self, *elements):
        self._elements = deque(elements)
 
    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()


# Initializing Class: Stack(Queue)
class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()


# Initializing Class: Priority Queue
class PriorityQueue(IterableMixin):
    def __init__(self):
        self._elements = []
        self._counter = count()

    def enqueue_with_priority(self, priority, value):
        element = (-priority, next(self._counter), value)
        heappush(self._elements, element)
        # heappush(self._elements, (priority, value))
        # Making the priority a negative number so that 
        # the highest one becomes the lowest
        # heappush(self._elements, (-priority, value))

    def dequeue(self):
        # return heappop(self._elements)
        # return heappop(self._elements)[1]
        return heappop(self._elements)[-1]



# Initializing Class: MutableMinHeap
@dataclass(order=True)
class Element:
    priority: float
    count: int
    value: any


class MutableMinHeap(IterableMixin):
    def __init__(self):
        super().__init__()
        self._elements_by_value = {}
        self._elements = []
        self._counter = count()

    def __setitem__(self, unique_value, priority):
        if unique_value in self._elements_by_value:
            self._elements_by_value[unique_value].priority = priority
            heapify(self._elements)
        else:
            element = Element(priority, next(self._counter), unique_value)
            self._elements_by_value[unique_value] = element
            heappush(self._elements, element)
            

        