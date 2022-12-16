# Representing Priority Queues With a Heap

# -------- DEMO 1
from heapq import heappush

print("\n\n\n" + ("="*60) + "\n\n\tRepresenting Priority Queues With a Heap\n\n" + ("="*60))

# List
fruits = []

heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")

# Displaying fruits
print("\n\n\t⭐ DEMO 1 - Heap push\n" + ("-"*60) + "\n")
print("\t", fruits)
print("\n" + ("-"*60))


# -------- DEMO 2
from heapq import heappop

# Popping elements
print("\n\n\n\t⭐ DEMO 2 - Heap pop\n" + ("-"*60) + "\n")
print(f"\t{'Popped Element:':<25s}", heappop(fruits))

# Displaying elements
print(f"\t{'Remaining Element/s:':<25s}", fruits)


# -------- DEMO 3
person1 = ("John", "Brown", 42)
person2 = ("John", "Doe", 42)
person3 = ("John", "Doe", 24)

# Display tuple comparison
print("\n\n\n\t⭐ DEMO 3 - Tuple Comparison\n" + ("-"*60) + "\n")
print("\t", person1 < person2)
print("\t", person2 < person3)

print("\n" + ("="*60) + "\n\n\n")
