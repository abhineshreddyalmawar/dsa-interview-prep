# INDEPENDENT NEETCODE PRACTICE - DAY 1 (Aug 10, 2026) | Two Sum
# First solo/cold attempt at a NeetCode 150 problem - untimed, reviewed and rebuilt together after

# --- enumerate() : gives index + value together, list's version of dict's .items() ---
nums = [2, 7, 11, 15]
for i, num in enumerate(nums):
    print(i, num)

# --- Two Sum : same core pattern as Day 1's Contains Duplicate, applied differently ---
# Question at each step: "have I already seen the OTHER number I'd need to reach target?"
# complement = target - num  ->  recalculated fresh every iteration
def two_sum(nums, target):
    seen = {}                          # value -> index, same role as Day 1's "seen" dict
    for i, num in enumerate(nums):
        complement = target - num       # what partner number would complete the pair
        if complement in seen:           # checks KEYS only, same as any dict `in` check
            return [seen[complement], i]  # [earlier position, current position]
        seen[num] = i                    # not found yet - remember this number's position

print(two_sum([2, 7, 11, 15], 9))
# [0, 1]

print(two_sum([3, 2, 4], 6))
# [1, 2]