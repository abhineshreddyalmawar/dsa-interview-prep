# python_practice28.py  --  Oct 26, 2026 (Monday, revision week day 1)
# Problem: Contains Duplicate (taught again from the idea up, then rebuilt by me)
# Result: Accepted 34/34, 38 ms (beats 100%), memory 13.9 MB (beats 62.26%).

from typing import List

# ---------------------------------------------------------------
# The six questions
#   1. Name:    Contains Duplicate
#   2. Does:    checks whether any number appears more than once
#   3. Input:   a list of whole numbers (nums: List[int])
#   4. Output:  True or False (bool)
#   5. Steps every time: say it in one sentence; name input and output with a tiny example;
#      ask "what do I need to remember?"; pick the tool; stage comments, then code;
#      trace the smallest input; say time and space.
#   6. Algorithm (the five jobs):
#        1. PREPARE    -> seen = set()   the notebook, empty, made ONCE before the loop
#        2. GO THROUGH -> for num in nums
#        3. DECIDE     -> if num in seen: return True   (a repeat: stop and answer)
#        4. UPDATE     -> seen.add(num)                 (write this number in the notebook)
#        5. RETURN     -> return False   after the loop, lined up with the 'for'
#
# Why a set: the key question is "have I seen this number before?"
#   Only a yes or no, nothing attached to each number, so the notebook is a set.
#   "duplicate / more than once / seen before" -> set.
# ---------------------------------------------------------------


class ContainsDuplicate:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False


# Trace (my own, for [1, 2, 3, 3]):
#   1: not in seen -> add  {1}
#   2: not in seen -> add  {1, 2}
#   3: not in seen -> add  {1, 2, 3}
#   3: in seen -> return True (the loop stops at the last position)
#   If the loop ends with no repeat, return False.
#
# Complexity: time O(n): the loop runs once for every number, and each round is one step,
#               because 'num in seen' and 'seen.add(num)' are set operations that jump
#               straight to the answer (O(1)). A list 'in' would scan the list (O(n) each).
#             space O(n): the seen set grows with the input; in the worst case (no duplicate)
#               it holds all n numbers. Big O describes the worst case.
#
# Corrections today:
#   1. A one-step lookup is O(1), not O(n). The whole loop is O(n) because it does n lookups.
#   2. The round is cheap because the set jumps to the answer, not because "if or else, not both".
#   3. Two Sum preview: the notebook is a dict {number: position}, because the answer needs
#      the position attached to the number. Key = number, value = position.
#
# Interview sentence:
# "I keep a set of the numbers I have seen. For each number, if it is already in the set I
#  return True, otherwise I add it. If the loop ends, there was no duplicate, so False.
#  Time is O(n) and space is O(n)."

if __name__ == "__main__":
    print(ContainsDuplicate().hasDuplicate([1, 2, 3, 3]))   # True
    print(ContainsDuplicate().hasDuplicate([1, 2, 3, 4]))   # False
    print(ContainsDuplicate().hasDuplicate([]))             # False
    print(ContainsDuplicate().hasDuplicate([5]))            # False

# Next: Tue Oct 27: Valid Anagram (dict of counts). First, Contains Duplicate again from a blank editor, 10 minutes.
