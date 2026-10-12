# python_practice20.py  --  Oct 12, 2026 (Monday, new problem)
# Problem: Contains Duplicate (NeetCode 150, Arrays & Hashing)
# Result: Accepted 34/34. First submit with a list: 2088 ms (beats 1.70%).
#         Second submit with a set: 33 ms (beats 100.00%).

from typing import List

# ---------------------------------------------------------------
# PLAN
# Question: "have I seen this number before?"  ->  a SET.
#   1. make an empty set called seen
#   2. loop over each number
#   3. if the number is already in seen  -> return True (found a duplicate)
#   4. otherwise add it to seen and move on
#   5. after the loop ends, return False (nothing repeated)
# ---------------------------------------------------------------


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for number in nums:
            if number in seen:
                return True
            else:
                seen.add(number)
        return False


# ---------------------------------------------------------------
# What I learned today:
#   1. A list works, but "number in list" scans every item, so the whole
#      loop is O(n^2). Measured: 2088 ms. A set jumps straight to the item:
#      one check is O(1), the whole loop is O(n). Measured: 33 ms.
#   2. seen = {}  makes an empty DICT, not a set. A dict has no .add.
#      An empty set is written set().
#   3. list uses .append(x); set uses .add(x).
#   4. return False goes AFTER the loop: only then do we know nothing repeated.
#   5. No semicolon needed in Python.
#
# List vs set:
#   list: ordered, allows repeats, lookup O(n), less memory
#   set:  no order, no repeats, lookup O(1) on average, a bit more memory
#   Trade-off: the set is faster but uses more memory and loses order.
#   Order does not matter here, so the set is the right choice.
#
# Complexity: time O(n), space O(n) (the set can hold every number).
#
# Interview sentence (model, to be said in my own words):
# "I used a set because I only need to ask whether I've seen a number before,
#  and a set answers that in constant time, so the whole loop is O(n)
#  instead of O(n squared). The cost is extra memory for the set."
# ---------------------------------------------------------------

if __name__ == "__main__":
    print(Solution().hasDuplicate([1, 2, 3, 1]))  # True
    print(Solution().hasDuplicate([1, 2, 3, 4]))  # False

# Next: repeat Contains Duplicate on Thu Oct 15 from a blank editor.
