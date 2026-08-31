# PHASE A - DAY 1 (Jul 24, 2026) | String Methods & Formatting + try/except
# Real-world tie-in: NexusAI - cleaning messy repo tech-stack text, handling errors gracefully (CCA-F link)

# --- .split() : turns ONE string into a LIST, cut at a separator ---
raw_stack = "  python, Flask , postgresql  "
pieces = raw_stack.split(",")
# cuts at every comma; does NOT remove spaces, only the comma itself
print(pieces)
# ['  python', ' Flask ', ' postgresql  ']

# --- loop + .strip().lower() : cleaning each piece ---
clean_stack = []
for item in pieces:                  # item = one messy piece, e.g. ' Flask '
    cleaned = item.strip().lower()   # strip() = edge whitespace only, lower() = case, chained left to right
    clean_stack.append(cleaned)      # .append() adds it to the end of clean_stack
print(clean_stack)
# ['python', 'flask', 'postgresql']

# --- try/except : handle errors without crashing (CCA-F structured error handling, code-level) ---
try:
    result = 10 / 0              # would normally crash with ZeroDivisionError
except ZeroDivisionError:        # catch that specific error type
    print("Can't divide by zero")
print("Still running")           # proof the program kept going, didn't crash
