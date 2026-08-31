# PHASE B - DAY 5 (Aug 5, 2026) | Sorting & Big-O Intuition
# Real-world tie-in: ranking NexusAI's analyzed repos by rating for a recruiter report

# --- Selection Sort : repeatedly find the max, move it out - O(n^2) ---
numbers = [5, 2, 8, 1, 9]
sorted_numbers = []

while numbers:                        # non-empty list = truthy, keeps looping
    biggest = max(numbers)             # built-in - same idea as Day 2's max-finder
    sorted_numbers.append(biggest)
    numbers.remove(biggest)            # removes by VALUE (contrast: .pop() removes by POSITION)

print(sorted_numbers)
# [9, 8, 5, 2, 1]

# --- Big-O reasoning : O(n) work, done n times ---
# round 1: O(n) scan | round 2: O(n-1) | ... | last: O(1)
# total = n + (n-1) + ... + 1  ≈  n^2 / 2  →  O(n^2) (constants dropped in Big-O)
# n=1000 → ~500,000 actual operations, not 1,000,000 - Big-O drops the /2 but the real number matters practically

# --- built-in sort : what you'd actually use in real code ---
ratings = [7, 3, 9, 1]

top_rated = sorted(ratings)           # returns a NEW list, ORIGINAL untouched
print(top_rated)                      # [1, 3, 7, 9]
print(ratings)                        # [7, 3, 9, 1] -- unchanged, proves sorted() doesn't modify in place

ratings.sort()                        # sorts IN PLACE, changes the original, returns None
print(ratings)                        # [1, 3, 7, 9] -- now it IS changed

descending = sorted(ratings, reverse=True)
print(descending)                     # [9, 7, 3, 1]