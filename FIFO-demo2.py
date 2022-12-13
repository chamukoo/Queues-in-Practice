from queues import Queue

fifo = Queue("1st", "2nd", "3rd")

# Display the length 
print(len(fifo))

# Displaying the Elements
for element in fifo:
    print(element)
