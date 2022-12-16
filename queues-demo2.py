# Stack: Last-In, First-Out (LIFO)

from mod.queues import Stack

print("\n\n\n" + ("="*60) + "\n\n\t  Stack: Last-In, First-Out (LIFO)\n\n" + ("="*60))

# -------- DEMO 1
lifo = Stack("1st", "2nd", "3rd")

# Display the elements in reverse
print("\n\n\t⭐ DEMO 1 - Display Elements Using for Loop\n" + ("-"*60) + "\n")
for element in lifo:
    print("\t", element)
print("\n" + ("-"*60))

# -------- DEMO 2
# List
lifo = []

# Append elements in list
lifo.append("1st")
lifo.append("2nd")
lifo.append("3rd")

# Display and pop elements
print("\n\n\n\t⭐ DEMO 2 - Display Dequeued Elements\n" + ("-"*60) + "\n")
print("\t", lifo.pop())
print("\t", lifo.pop())
print("\t", lifo.pop())

print("\n" + ("="*60) + "\n\n\n")
