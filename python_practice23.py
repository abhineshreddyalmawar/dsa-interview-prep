# python_practice23.py  --  Oct 15, 2026 (Thursday, repeats and a list-vs-set exercise)
# Problems: Contains Duplicate (repeat), Valid Anagram (repeat), dedupe exercise
# Results: Contains Duplicate Accepted, 32 ms. Valid Anagram Accepted 37/37, 51 ms.
# Both repeats passed first try from a blank editor, with stage comments I wrote myself.

from typing import List

# ---------------------------------------------------------------
# Contains Duplicate (repeat)
# PLAN
#   1. seen = set()                 -> one-step "have I seen this?" lookups
#   2. for number in nums
#   3. if number in seen: return True
#   4. else: seen.add(number)
#   5. after the loop: return False (lined up with the 'for')
# ---------------------------------------------------------------


class ContainsDuplicate:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for number in nums:
            if number in seen:
                return True
            else:
                seen.add(number)
        return False


# ---------------------------------------------------------------
# Valid Anagram (repeat)
# PLAN
#   1. if len(s) != len(t): return False   (different lengths cannot be anagrams)
#   2. count the letters of s in counts_s  (first time = 1, else + 1)
#   3. count the letters of t in counts_t
#   4. return counts_s == counts_t         (same counts, same letters)
# ---------------------------------------------------------------


class ValidAnagram:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts_s = {}
        counts_t = {}
        for char in s:
            if char in counts_s:
                counts_s[char] = counts_s[char] + 1
            else:
                counts_s[char] = 1
        for char in t:
            if char in counts_t:
                counts_t[char] = counts_t[char] + 1
            else:
                counts_t[char] = 1
        return counts_s == counts_t


# ---------------------------------------------------------------
# Dedupe exercise: remove repeated words, keep the first of each, keep the order
#   Slow version: 'if word not in result' scans the LIST each time -> O(n^2).
#   Fast version: check a SET instead, and still append to the list -> O(n).
#   Time O(n); space O(n) (the set and the result list both grow).
# ---------------------------------------------------------------


def dedupe(words):
    result = []
    seen = set()
    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    return result


# ---------------------------------------------------------------
# Lessons today:
#   1. Hidden loop: 'x in some_list' scans the list. Inside a for loop that is O(n^2).
#      A set or dict jumps straight to the answer (one step), so the code is O(n),
#      at the cost of extra memory.
#   2. list uses .append (a line you add to the end of); set uses .add (a bag you add into).
#   3. A dict/set does not "check everything at once": it jumps to the answer.
#   4. Space method: what new thing do I build, and how does it grow with the input?
#   5. Template: "Time is ___ because ___. Space is ___ because of ___."
# ---------------------------------------------------------------

if __name__ == "__main__":
    print(ContainsDuplicate().hasDuplicate([1, 2, 3, 1]))        # True
    print(ContainsDuplicate().hasDuplicate([1, 2, 3, 4]))        # False
    print(ValidAnagram().isAnagram("racecar", "carrace"))        # True
    print(ValidAnagram().isAnagram("jar", "jam"))                # False
    print(dedupe(["a", "b", "a", "c", "b"]))                     # ['a', 'b', 'c']

# Next: Top K Frequent and Longest Consecutive Sequence from a blank editor on Fri Oct 16.
