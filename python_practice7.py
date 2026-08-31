# PHASE B - DAY 1 (Jul 30, 2026) | Stacks & Queues
# Real-world tie-in: undo history (stack), boarding line (queue), Valid Parentheses problem

# --- stack : LIFO, last in first out ---
undo_stack = []
undo_stack.append("typed 'hello'")   # .append() = push onto the stack
undo_stack.append("typed 'world'")
last_action = undo_stack.pop()       # .pop() = remove + return the LAST item
print(last_action)                   # typed 'world'

# --- queue : FIFO, first in first out ---
boarding_line = []
boarding_line.append("Abhinesh")     # .append() = same as before, add to back of line
boarding_line.append("Priya")
next_passenger = boarding_line.pop(0)  # .pop(0) = remove + return the FIRST item
print(next_passenger)                  # Abhinesh

# --- Valid Parentheses : classic stack problem ---
def is_valid(s):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in "([{":              # opener -> push it, wait for its match
            stack.append(char)
        else:                          # closer -> must match the top of the stack
            if not stack:               # nothing to match against -> invalid
                return False
            top = stack.pop()
            if top != pairs[char]:      # popped opener doesn't match this closer -> invalid
                return False

    return len(stack) == 0             # leftover unclosed openers -> invalid

print(is_valid("({[]})"))   # True
print(is_valid(")"))        # False -- empty-stack guard catches this before crashing
print(is_valid("(("))       # False -- len(stack)==0 check catches unclosed openers