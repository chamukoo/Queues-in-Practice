# Queues: Firs-In, First-Out (FIFO)

from collections import deque

# Initializing Class
class Queue:
    def __init__(self):
        self._elements = deque()

    def enqueue(self, element):
        self._elements.append(element)

    