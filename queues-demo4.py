# Building a Priority Queue Data Type

from mod.queues import PriorityQueue

print("\n\n\n" + ("="*60) + "\n\n\t\tBuilding a Priority Queue Data Type\n\n" + ("="*60))

# Defined Priority Levels
CRTICAL = 3
IMPORTANT = 2
NEUTRAL = 1

messages = PriorityQueue()


# -------- DEMO 1
messages = PriorityQueue()
messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages.enqueue_with_priority(CRTICAL, "Brake pedal depressed")
messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

# Dequeing messages from the highest priority
print("\n\n\n\t⭐ DEMO 1 - Highest Priority First\n" + ("-"*60) + "\n")
print("\t", messages.dequeue())
print("\t", messages.dequeue())
print("\t", messages.dequeue())
print("\t", messages.dequeue())

print("\n" + ("="*60) + "\n\n\n")
