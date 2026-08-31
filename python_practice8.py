# PHASE B - DAY 2 (Jul 31, 2026) | Linked Lists
# Real-world tie-in: train cars hooked together - each node points to the next, no positional shortcut

# --- Node : the building block (value + pointer to the next node) ---
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None    # not connected to anything yet

# --- chaining nodes together ---
first_car = Node("Engine")
second_car = Node("Passenger Car")
third_car = Node("Dining Car")

first_car.next = second_car     # points to the actual object, doesn't copy data
second_car.next = third_car

print(first_car.next.value)         # Passenger Car
print(first_car.next.next.value)    # Dining Car -- walking 2 hops

# --- traversal : walk the whole chain with a while loop ---
current = first_car
while current is not None:      # loops until we fall off the end (next = None)
    print(current.value)
    current = current.next      # move one hop forward
# Engine / Passenger Car / Dining Car

# --- insert at the FRONT : O(1), rewire ONE connection, no shifting ---
new_engine = Node("New Engine")
new_engine.next = first_car     # new node points to the old front
# new_engine is now the front -- first_car and everything after is untouched

current = new_engine
while current is not None:
    print(current.value)
    current = current.next
# New Engine / Engine / Passenger Car / Dining Car