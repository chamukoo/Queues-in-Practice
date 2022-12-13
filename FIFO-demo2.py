from queues import Queue

fifo = Queue("1st", "2nd", "3rd")

# Display the length 
print(len(fifo))

# Displaying the Elements
for element in fifo:
    print(element)

# The queue has 3 elements initially, but its length
# drops to 0 after consuming all elements in a loop.
print(len(fifo))
