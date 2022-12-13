from queues import Queue

fifo = Queue()

# Adding Default Elements
fifo.enqueue('1st')
fifo.enqueue('2nd')
fifo.enqueue('3rd')

# Displaying Popped Elements
print(fifo.dequeue())
print(fifo.dequeue())
print(fifo.dequeue())