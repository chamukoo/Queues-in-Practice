#Queue: First-In, First-Out (FIFO)

from mod.queues import Queue

print("\n\n\n" + ("="*60) + "\n\n\tQueue: First-In, First-Out (FIFO)\n\n" + ("="*60))

# -------- DEMO 1
fifo = Queue()

# Adding Default Elements
fifo.enqueue('1st')
fifo.enqueue('2nd')
fifo.enqueue('3rd')

# Displaying Popped Elements
print("\n\n\tDEMO 1 - Display Dequeued Elements\n" + ("-"*60) + "\n")
print("\t", fifo.dequeue())
print("\t", fifo.dequeue())
print("\t", fifo.dequeue())
print("\n" + ("-"*60))


# -------- DEMO 2
fifo = Queue("1st", "2nd", "3rd")

# Display the length 
print("\n\n\n\tDEMO 2.0 - Display Length\n" + ("-"*60) + "\n")
print("\t", len(fifo))
print("\n" + ("-"*60))

# Displaying the Elements
print("\n\n\n\tDEMO 2.1 - Display Element Using for Loop\n" + ("-"*60) + "\n")
for element in fifo:
    print("\t", element)
print("\n" + ("-"*60))

# The queue has 3 elements initially, but its length
# drops to 0 after consuming all elements in a loop.
print("\n\n\n\tDEMO 2.2 - Length Drops to 0\n" + ("-"*60) + "\n")
print("\t", len(fifo))

print("\n" + ("="*60) + "\n\n\n")
