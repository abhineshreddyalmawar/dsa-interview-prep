# python_practice18.py  --  Oct 8, 2026 (Thursday, repeat day)
# Problem: Valid Anagram, from a blank editor (NeetCode 150)
# Repeat of Oct 6. Today: slow list version first, then the dict-loop version.

from collections import Counter

# ---------------------------------------------------------------
# PLAN (said before coding)
# Two words are anagrams if they use the same letters the same number of times.
#
# Version 1 (slow): walk through t. For each letter, find it in s and REMOVE it.
#   Letter not found -> False. All found -> True.
#   Length check is REQUIRED: the loop only walks t, so leftover letters
#   in s are never seen.
#   Cost: O(n^2). "char in s" scans the list, and .remove() scans it again.
#
# Version 2 (dict loop): count the letters of each word in a dict.
#   key = ONE letter, value = how many times it appears.
#   For each letter: already a key -> add 1, else -> set to 1.
#   Anagrams -> the two dicts are equal (key order doesn't matter).
#   Length check is only an OPTIMIZATION: comparing the full dicts catches
#   any extra letter or count difference automatically.
#   Cost: O(n). Each word is handled ONCE.
#
# Version 3: Counter(s) == Counter(t)   (the dict loop in one line)
# ---------------------------------------------------------------


class Solution:
    # ---- Version 1: list + remove (slow, O(n^2)) ----
    def isAnagram_slow(self, s: str, t: str) -> bool:
        if len(s) != len(t):        # REQUIRED here
            return False
        s = list(s)                 # a string has no .remove(), a list does
        for char in t:
            if char in s:
                s.remove(char)      # remove the letter we are looking at
            else:
                return False        # capital F
        return True

    # ---- Version 2: dict loop (O(n)) ----
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):        # optimization only: early exit
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

    # ---- Version 3: Counter (same job, one line) ----
    def isAnagram_counter(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


# ---------------------------------------------------------------
# Bugs I made and fixed today (remember these):
#   1. Signature: def isAnagram(self, s: str, t: str) -> bool:
#      (name: type, separated by commas)
#   2. Colons only end lines that START a block (def, if, else, for).
#      Never after a return.
#   3. Python's words are lowercase if, and True / False with capitals.
#   4. s.remove() needs the letter inside: s.remove(char)
#   5. list() is EMPTY. list(s) keeps the letters of s.
#      (I wiped s and t by writing s = list())
#   6. The comparison/return from Group Anagrams does not belong here:
#      Group Anagrams key = sorted word, value = list of words.
#      Valid Anagram key = ONE letter, value = a count.
#   7. In the if check, use the dict you are BUILDING:
#      count_s in the loop over s, count_t in the loop over t.
#   8. count_s[char] = count_s[char] + 1   (update one entry, not the dict)
#   9. Real code, not comments: the for / if / else lines must not sit
#      behind a #.
# ---------------------------------------------------------------

# Key facts:
#   Length check: REQUIRED in the .remove() version, OPTIMIZATION in the dict version.
#   "ab" vs "abc": count_t has an extra key "c", so the dicts differ -> False
#   even with no length check.

# Interview sentence:
# "I counted the letters of each word in a dict, with the letter as the key and
#  the count as the value. If the words are anagrams the two dicts are equal,
#  and each word is handled once, so it is O(n) instead of O(n^2)."

# Pattern table:
#   "How many of each?" -> dict of counts / Counter

if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("racecar", "carrace"))   # True
    print(sol.isAnagram("jar", "jam"))           # False
    print(sol.isAnagram_slow("anagram", "nagaram"))   # True
    print(sol.isAnagram_counter("rat", "car"))        # False

# Next: Group Anagrams from a blank editor on Friday (repeat).
# Valid Anagram returns about 2 weeks later.
