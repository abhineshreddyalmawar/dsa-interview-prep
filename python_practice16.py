# DAY 4 (Oct 6, 2026) | NeetCode: Valid Anagram (slow version + Counter version) + System Design: Databases & Indexing
# Real-world tie-in: a rail booking site finding ONE booking among 50 million by confirmation code

# --- NEETCODE SOLO PRACTICE : Valid Anagram ---
# anagram = same letters, same counts, any order -> "racecar"/"carrace" is True, "jar"/"jam" is False
# this is my Aug 11 slow version, retyped from a blank editor - it passed the example but had a hidden bug (see below)
# how to start any problem: write the steps as plain-English comments first, then turn each into 1-3 lines of code

class Solution:                                    # LeetCode wraps the answer in a class named Solution (capital S)
    def isAnagram(self, s: str, t: str) -> bool:   # method name must be isAnagram; self is always the first parameter
        if len(s) != len(t):                       # different lengths can NEVER be anagrams - stop early
            return False                           # this 2-line check fixes the bug: without it "aab" vs "ab" wrongly returned True
        a = list(s)                                # string -> list, because a list has .remove()
        b = list(t)                                # same for t
        for char in b:                             # walk through every letter of t
            if char in a:                          # is this letter still available in s?
                a.remove(char)                     # use it up: .remove(value) deletes ONE copy, found by value
            else:
                return False                       # letter missing (or already used up) -> not an anagram
        return True                                # every letter of t matched a letter of s

# to test locally, call it through an object: Solution().isAnagram(...) - on LeetCode, skip the print lines
print(Solution().isAnagram("racecar", "carrace"))  # NeetCode example 1
# True
print(Solution().isAnagram("jar", "jam"))          # NeetCode example 2
# False
print(Solution().isAnagram("aab", "ab"))           # the bug case: s has an extra "a" - the length check catches it
# False

# the bug, traced by hand (no length check): a = ['a','a','b'], t = "ab" -> removes 'a', then 'b', loop ends
# one 'a' is left over in a but the loop only walks t, so it never notices -> wrongly returns True
# first error today: NameError - is_anagram was defined INSIDE class Solution, so a bare is_anagram(...) call can't find it

# O(n^2): `char in a` and .remove() each scan the list, and both run inside a loop of n letters
# next (Thursday, from a blank editor): the O(n) dict-counting version, same pattern as Day 2's city_counts
#   1. length check (done)   2. empty dict   3. loop over s, add 1 per letter   4. loop over t, subtract 1   5. all counts 0 -> True


# --- NEETCODE ADDITIONAL SOLUTION : Valid Anagram, the modern Pythonic way (collections.Counter) ---
# same problem, same answer, one line of logic - this is how it is usually written in real Python code today
# found with NeetBot's help AFTER my own version passed, so this is the reference version, NOT a cold solve
# Thursday's blank-editor repeat is still the real test

from collections import Counter                    # Counter lives in the collections module; import it to run locally (LeetCode may pre-import it, don't rely on that)

class SolutionCounter:                             # different name only so this file can hold both versions; on LeetCode it must be class Solution
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):                       # same early exit as before: different lengths can never be anagrams
            return False
        return Counter(s) == Counter(t)            # Counter(s) = dict-like {letter: how many times}; == compares the two count tables

print(Counter("racecar"))                          # a Counter is a dict that counts for you - same job as my city_counts loop on Day 2
# Counter({'r': 2, 'a': 2, 'c': 2, 'e': 1})
print(SolutionCounter().isAnagram("racecar", "carrace"))   # NeetCode example 1: same letters, same counts
# True
print(SolutionCounter().isAnagram("jar", "jam"))   # counts differ: 'r' in one string, 'm' in the other
# False

# O(n) time: one pass over each string to count, then compare the two tables
# O(n) extra space in general; with lowercase-only input there are at most 26 letters, so practically O(1)
# slow version O(n^2) -> Counter O(n): the speed-up comes from counting each string once instead of searching a list for every letter
# Counter(s) is the same counting as the hand-written dict loop (steps 2-4 of Thursday's plan), wrapped in one call
# interview note: know BOTH - write the dict loop by hand if asked "without Counter", and say "Counter does exactly this" when using it
# without the length check this still gives the right answer; the check is only an early exit that saves building two counters


# --- SYSTEM DESIGN : Databases & Indexing ---
# why a database: data lives on disk (survives restarts) and every server can share it - fixes yesterday's "state in one server's memory"
# without an index: full scan = check every row until the match -> O(n)  (10 million rows -> up to 10 million checks)
# with an index: a separate SORTED structure maps value -> row location -> O(log n)  (10 million rows -> about 24 steps)
# each step throws away about half of what's left - same idea as a BST (smaller goes left, bigger goes right)
# real databases use a B-tree: a BST relative with many keys per node, so fewer disk reads

import math                                        # math.log2(n) = how many times n can be halved down to 1

for rows in [1000, 2000, 1000000, 10000000]:       # table sizes to compare
    steps = math.ceil(math.log2(rows))             # ceil rounds UP - a partial step still costs a whole step
    print(rows, "rows -> up to", rows, "checks without an index, about", steps, "steps with one")
# 1000 rows -> up to 1000 checks without an index, about 10 steps with one
# 2000 rows -> up to 2000 checks without an index, about 11 steps with one
# 1000000 rows -> up to 1000000 checks without an index, about 20 steps with one
# 10000000 rows -> up to 10000000 checks without an index, about 24 steps with one
# doubling the data (1000 -> 2000) adds only ONE step - that is what O(log n) means

# cost of an index: (1) extra storage  (2) SLOWER WRITES - every insert/update must also update the index; reads get FASTER, not slower
# a primary key (e.g. a unique ID) is indexed automatically; index other columns only if you search by them often
# VerifyHire: results are written once per analysis and read many times (every reload) -> slower writes cost little, so the index is worth it
# DS&A link: BST in-order traversal is sorted (Aug 3 log) - that sortedness is exactly what makes an index fast
