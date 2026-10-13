# python_practice21.py  --  Oct 13, 2026 (Tuesday, new problem)
# Problem: Top K Frequent Elements (NeetCode 150, Arrays & Hashing)
# Result: Accepted 99/99. Runtime 232 ms (beats 29.66%), memory 13.7 MB (beats 100%).
# Needed a lot of guidance: built in three small steps (count, order, take).
# Rewrite from a stage-comment skeleton the same day: Accepted 99/99, 168 ms (beats 79.89%).

from typing import List

# ---------------------------------------------------------------
# PLAN
#   1. COUNT:  dict, number -> how many times it appears
#   2. ORDER:  turn the dict into (number, count) pairs, sort by count, biggest first
#   3. TAKE:   keep the first k pairs, return only the NUMBERS (pair[0])
# ---------------------------------------------------------------


class Solution:
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


# ---------------------------------------------------------------
# Bugs and lessons today:
#   1. I pasted my Group Anagrams code. Different problem, different shape:
#      here the dict VALUE is a plain integer count, not a list.
#   2. counts[number] = [1]  ->  counts[number] = 1  (a list + 1 is a TypeError)
#   3. Branches swapped: "already in counts" adds 1; "first time" starts at 1.
#   4. Variables only exist inside the function that creates them (NameError),
#      so the new lines must sit at the same indentation as the for loop.
#   5. pair[0] is the number, pair[1] is the count. I returned pair[1] first.
#      NeetCode's first example hid it, because number == count there
#      ((3,3), (2,2)). The example [7, 7], k = 1 exposed it: my answer was [2],
#      the right answer is [7]. Always test with my own example too.
#   6. sorted(..., key=lambda pair: pair[1], reverse=True) sorts by the count.
#   7. ordered[:k] takes the first k items (slicing).
#   8. Rewrite bug: 'return result' indented INSIDE the for loop returned after
#      the first pair, so every answer was one item short ([4] instead of [4, 7]).
#      Fix: line 'return' up with the 'for' so it runs AFTER the loop.
#
# Complexity: time O(n log n) overall: counting is O(n); sorting the unique
# numbers costs the most, O(m log m) where m <= n. Space O(n) for the dict.
# (A faster way exists with buckets, O(n); a later improvement.)
#
# Interview sentence (model, to say in my own words):
# "I count how often each number appears with a dict, sort the (number, count)
#  pairs by count from highest to lowest, and return the numbers of the first k.
#  Counting is O(n) and the sort makes it O(n log n); the dict costs O(n) memory."
# ---------------------------------------------------------------

if __name__ == "__main__":
    print(Solution().topKFrequent([1, 2, 2, 3, 3, 3], 2))  # [3, 2]
    print(Solution().topKFrequent([7, 7], 1))              # [7]
    print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]

# Next: repeat Top K Frequent on Fri Oct 16 from a blank editor.
