# PHASE A - DAY 3 (Jul 28, 2026) | dict.get() + List/Dict Comprehensions
# Real-world tie-in: NexusAI - safe lookups, compact filtering of repos/results

# --- dict.get() : safe lookup, never crashes (vs dict[key]) ---
coat_check = {"Abhinesh": "Grey Nissan"}
print(coat_check.get("Abhinesh"))              # key exists -> value
print(coat_check.get("Rahul"))                 # missing key -> None, no crash
print(coat_check.get("Rahul", "No coat found"))  # missing key -> custom default

# --- list comprehension : [expr for item in list] = manual loop + append, one line ---
numbers = [1, 2, 3, 4, 5]
doubled = [n * 2 for n in numbers]
print(doubled)
# [2, 4, 6, 8, 10]

# --- list comprehension + filter : [expr for item in list if condition] ---
names = ["Abhinesh", "Al", "Priya", "Jo"]
long_names = [name for name in names if len(name) > 3]
print(long_names)
# ['Abhinesh', 'Priya']

# --- % (modulo) : remainder after division, standard even/odd check ---
evens = [n for n in numbers if n % 2 == 0]
print(evens)
# [2, 4]  (only even numbers from 1-5)

# --- dict comprehension : {key: value for item in list if condition} ---
prices = {"apple": 3, "banana": 1, "mango": 5}
expensive = {item: price for item, price in prices.items() if price > 2}
print(expensive)
# {'apple': 3, 'mango': 5}