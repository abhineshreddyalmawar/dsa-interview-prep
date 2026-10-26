# python_practice28.py  --  Oct 26, 2026 (Monday, revision week day 1)
# Problems: Contains Duplicate (taught again from the idea up, then rebuilt by me)
#           Valid Anagram (bonus: first try on my own with the notebook table, taught properly Tue)
# Results: Contains Duplicate Accepted 34/34, 38 ms (beats 100%), memory 13.9 MB (beats 62.26%).
#          Valid Anagram Accepted 37/37, 80 ms (beats 15.20%), memory 8.5 MB (beats 60.08%).

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

# ---------------------------------------------------------------
# Valid Anagram (bonus, first try on my own)
#   1. Name:   Valid Anagram
#   2. Does:   checks whether t is made of exactly the same letters as s, in any order,
#              each letter used the same number of times
#   3. Input:  two strings, s and t
#   4. Output: True or False
#   Key question: what must I remember about each letter? How many times it appears.
#   Not a yes/no (so not a set); a number attached to each letter -> dict, letter to count.
#   Order does not matter ("racecar" and "carrace" are anagrams), so comparing position by
#   position is the wrong method; comparing counts is the right one.
#   The five jobs:
#     1. PREPARE    -> a length check first (different lengths: return False),
#                      then two empty dicts, count_s and count_t
#     2. GO THROUGH -> for char in s, then for char in t
#     3. DECIDE     -> if char is already in the dict
#     4. UPDATE     -> yes: count + 1; no: count = 1 (first time)
#     5. RETURN     -> count_s == count_t, after both loops
# ---------------------------------------------------------------


class ValidAnagram:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = {}
        count_t = {}
        for char in s:
            if char in count_s:
                count_s[char] = count_s[char] + 1
            else:
                count_s[char] = 1
        for char in t:
            if char in count_t:
                count_t[char] = count_t[char] + 1
            else:
                count_t[char] = 1
        return count_s == count_t


# Trace for "jar" and "jam":
#   count_s = {j: 1, a: 1, r: 1}   count_t = {j: 1, a: 1, m: 1}   r vs m differ -> False
#
# Slips fixed today:
#   1. count was made as 'dict' (the type) instead of an empty dict {}:
#      "TypeError: 'type' object does not support item assignment".
#   2. The key was the whole string (count_s[s]) instead of the current letter (count_s[char]).
#   3. The test call had "s=racecar" inside the quotes, which made it a 9-character string.
#      Inside a call, write only the words: isAnagram("racecar", "carrace").
#   4. A comment said "if r in count_t" for "jam"; the letters are j, a, m.
#   5. Compared by position at first; anagrams ignore order, so count the letters instead.
#
# Complexity: time O(n): two loops one after the other (n + n = 2n, drop the constant),
#               and each dict check and update is one step (O(1)).
#             space O(1) for lowercase letters, O(k) in general: a dict holds one entry per
#               DIFFERENT letter, not per character ("aaaaaaaaaa" is one entry, {a: 10}),
#               and lowercase letters give at most 26. (O(n) is a safe upper bound only.)
#
# Interview sentence:
# "I count how many times each letter appears in both strings using two dicts, after a quick
#  check that the lengths match, then I compare the dicts. Time is O(n), space is O(1) for
#  lowercase letters because the dicts hold at most 26 entries."

if __name__ == "__main__":
    print(ContainsDuplicate().hasDuplicate([1, 2, 3, 3]))   # True
    print(ContainsDuplicate().hasDuplicate([1, 2, 3, 4]))   # False
    print(ContainsDuplicate().hasDuplicate([]))             # False
    print(ContainsDuplicate().hasDuplicate([5]))            # False
    print(ValidAnagram().isAnagram("racecar", "carrace"))   # True
    print(ValidAnagram().isAnagram("jar", "jam"))           # False

# Next: Tue Oct 27: Contains Duplicate again from a blank editor (10 minutes), then
# Valid Anagram taught properly from the idea up and rebuilt from a blank editor.
