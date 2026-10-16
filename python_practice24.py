# python_practice24.py  --  Oct 16, 2026 (Friday, repeats from a blank editor)
# Problems: Top K Frequent Elements (repeat), Longest Consecutive Sequence (repeat)
# Results: Top K Frequent Accepted 99/99, 156 ms (beats 95.40%).
#          Longest Consecutive Sequence Accepted 34/34, 51 ms (beats 81.09%).
# Stage comments written by me first; a few small slips fixed from hints.

from typing import List

# ---------------------------------------------------------------
# Top K Frequent Elements (repeat)
# PLAN
#   1. counts = {}                           -> dict, number -> how many times
#   2. for number in nums: if in counts, +1; else = 1
#   3. ordered = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
#   4. result = [] ; for pair in ordered[:k]: result.append(pair[0])
#   5. return result, lined up with the first 'for' (after the counting loop)
# ---------------------------------------------------------------


class TopK:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for number in nums:
            if number in counts:
                counts[number] = counts[number] + 1
            else:
                counts[number] = 1
        ordered = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
        result = []
        for pair in ordered[:k]:
            result.append(pair[0])
        return result


# Slips fixed today:
#   1. 'ordered = counts.items(), ...' was missing sorted( ... ).
#   2. lambda syntax is  lambda pair: pair[1]  (colon, same name on both sides).
#   3. ordered[k:] skips the first k (the LEAST frequent); ordered[:k] keeps the first k.
#   4. .add is for a set, .append is for a list.
#   5. ordered, result and return were indented inside the counting loop, so the function
#      returned after the first number. The [7, 7] test passed only by luck.
# Complexity: time O(n log n): counting is O(n), sorting is O(n log n), the slowest step wins.
#             space O(n): the dict holds up to n numbers.
# log n = how many times you can halve n (n = 8: 8->4->2->1 is 3 halvings, n log n = 24).


# ---------------------------------------------------------------
# Longest Consecutive Sequence (repeat)
# PLAN
#   1. Build = set(nums)                     -> one-step lookups
#   2. Best = 0                              -> the answer; also covers an empty list
#   3. for number in nums: key = number - 1
#   4. if key not in Build                   -> only the FIRST number of a chain counts
#   5. current = number ; length = 1
#   6. while current + 1 in Build: current + 1, length + 1
#   7. the while stops when current + 1 is NOT in Build (the chain ended)
#   8. if length > Best: Best = length       (after the while, inside the start block)
#      return Best, lined up with the 'for'
# ---------------------------------------------------------------


class LongestConsecutive:
    def longestConsecutive(self, nums: List[int]) -> int:
        Build = set(nums)
        Best = 0
        for number in nums:
            key = number - 1
            if key not in Build:
                current = number
                length = 1
                while current + 1 in Build:
                    current = current + 1
                    length = length + 1
                if length > Best:
                    Best = length
        return Best


# Slips fixed today:
#   1. Stage 7: the while stops when current + 1 is not in Build, not when nums runs out.
#   2. 'if length > Best' was inside the while body. For [1, 1, 1] the body never runs,
#      so Best stayed 0. It belongs after the while, inside the start block.
# Complexity: time O(n): the start check means each number is walked over about once
#             overall (for: n, while: about n in total, drop the constant).
#             space O(n): the set; current and length are single numbers (O(1)).
# O(n^2) space example: storing every pair (a, b) of the input, n x n entries.

if __name__ == "__main__":
    print(TopK().topKFrequent([1, 2, 2, 3, 3, 3], 2))              # [3, 2]
    print(TopK().topKFrequent([7, 7], 1))                          # [7]
    print(LongestConsecutive().longestConsecutive([100, 4, 200, 1, 3, 2]))   # 4
    print(LongestConsecutive().longestConsecutive([]))                       # 0
    print(LongestConsecutive().longestConsecutive([1, 1, 1]))                # 1
    print(LongestConsecutive().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9

# Next: Monday Oct 19 is a new problem, Product of Array Except Self.
