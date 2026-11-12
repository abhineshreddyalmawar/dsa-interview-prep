# python_practice38.py  --  Nov 12, 2026 (Thursday, week 2 of the new routine: 4 new problems a week)
# Problem: Permutation in String, LeetCode 567 (new problem; sliding window with a dict of counts and a
#          FIXED-size window; taught from the idea up, then written by me)
# Results: morning Accepted 43/43, 27 ms (beats 100.00%), memory 7.9 MB (beats 66.45%).
#          evening redo: SKIPPED today (no time); do it tomorrow morning from a blank editor.
#          complexity and the "because" below were given as a model today; say them in my own words tomorrow.

# ---------------------------------------------------------------
# The six questions
#   1. Name:    Permutation in String
#   2. Does:    checks whether s2 contains a CONNECTED piece that uses exactly the letters of s1 (all of
#               them, same counts), in any order
#   3. Input:   two strings, s1 and s2
#   4. Output:  a boolean: True or False, e.g. s1 = "ab", s2 = "eidbaooo" -> True (the piece "ba");
#               s1 = "ab", s2 = "eidboaoo" -> False
#   5. Steps every time: say it in one sentence; name input and output with a tiny example;
#      ask "what do I need to remember?"; pick the tool; stage comments, then code;
#      trace a tricky input; say time and space; derive the "because" from the trace.
#   6. Algorithm (the five jobs):
#        1. PREPARE    -> s1_counts (letter -> count for s1), counts = {} for the window, left = 0
#        2. GO THROUGH -> for right in range(len(s2))
#        3. UPDATE     -> the new letter enters the window: first time 1, otherwise + 1
#        4. DECIDE     -> while the window is longer than len(s1): (right - left + 1) > len(s1)
#        5. UPDATE     -> inside the while: counts[s2[left]] goes down by 1, if it is 0 then del that key,
#                         THEN left = left + 1
#        6. DECIDE     -> if counts == s1_counts: return True
#        7. RETURN     -> return False, after the loop
#
# Key question: what must I remember? How many times each letter appears in the window (a count attached
# to each letter, so a dict), compared with the same counts for s1; plus where the window's two fingers are.
#   "permutation / same letters any order / connected piece" -> a dict of counts plus a window of fixed
#   length len(s1): sliding window.
# ---------------------------------------------------------------


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = {}
        for char in s1:
            if char in s1_counts:
                s1_counts[char] = s1_counts[char] + 1
            else:
                s1_counts[char] = 1
        counts = {}
        left = 0
        for right in range(len(s2)):
            if s2[right] in counts:
                counts[s2[right]] = counts[s2[right]] + 1
            else:
                counts[s2[right]] = 1
            while (right - left + 1) > len(s1):
                counts[s2[left]] = counts[s2[left]] - 1
                if counts[s2[left]] == 0:
                    del counts[s2[left]]
                left = left + 1
            if counts == s1_counts:
                return True
        return False


# Trace for s1 = "abc", s2 = "lecaabee" (positions 0 to 7: l e c a a b e e), s1_counts {a:1, b:1, c:1}:
#   right 0-2: counts {l:1}, {l:1, e:1}, {l:1, e:1, c:1}; windows shorter than 3 or equal, no match
#   right 3 (a): enter -> {l:1, e:1, c:1, a:1} (4 letters, too long) -> l leaves: 0, del, left 1
#                -> {e:1, c:1, a:1}; no match
#   right 4 (a): enter -> {e:1, c:1, a:2}; e leaves: 0, del, left 2 -> {c:1, a:2}; no match
#   right 5 (b): enter -> {c:1, a:2, b:1}; c leaves: 0, del, left 3 -> {a:2, b:1}; no match
#   right 6 (e): enter -> {a:2, b:1, e:1}; a leaves: 2 -> 1, NOT deleted (still in the window),
#                left 4 -> {a:1, b:1, e:1}; no match
#   right 7 (e): enter -> {a:1, b:1, e:2}; a leaves: 1 -> 0, del, left 5 -> {b:1, e:2}; no match
#   return False (five leave steps, left goes 1, 2, 3, 4, 5)
#   Why del at 0: a window {x:0, c:1, a:1, b:1} is a real permutation of "abc", but the extra key x makes
#   == say "not equal"; the dict must describe exactly the letters that are in the window.
#   s1 longer than s2 ("abc", "ab"): the window never reaches 3 letters, counts never equals -> False.
#
# Slips fixed today:
#   1. Said the problem asks for "any common substring": it asks for a CONNECTED piece of s2 that uses ALL
#      the letters of s1 with the same counts, so its length is always len(s1).
#   2. Picked a set: a set loses counts ("aab" and "abb" both give {a, b}); counts are the thing two
#      permutations share (same as Valid Anagram) -> a dict of counts.
#   3. Suggested sorted letters: a correct idea but a sort for every window (slower); on a string it is
#      sorted(s1), not s1.sort().
#   4. Said what they share is "each letter appears once": true only for abc/cab; the real rule is the
#      same count for every letter.
#   5. Answered right = right + 1 when asked what happens to the dict: the entering letter adds 1 (first
#      time 1), the leaving letter subtracts 1; the fingers are a separate job.
#   6. Thought the dict equals s1's even with an extra key {x:0}: == compares keys too, so delete the key
#      at 0 (del counts[key]).
#   7. First code: for char in s (should be s1); for s2[right] in range(...) (should be for right in
#      range(...)); left-right+1 (should be right-left+1).
#   8. Indentation: the if/del lines sat outside the while, then left = left + 1 sat inside the if (left
#      moved only when a count reached 0, which breaks when a letter appears twice); fixed.
#   9. Trace: left values one short (1 to 5, five leave steps); compare after the del; the enter dict in
#      round 3 has 4 letters.
#
# Complexity (model given today; say it myself tomorrow):
#   Time O(n): right walks s2 once and left only moves forward, so each letter enters once and leaves at
#     most once; counts == s1_counts compares at most 26 keys, a fixed cost (about 26 times n, which is
#     O(n)); building s1_counts is O(len(s1)).
#   Space O(1): the two dicts hold at most 26 lowercase letters each, however long the strings are.
#
# I used X because Y (model given today; say it myself tomorrow):
# "I used a dict of counts with a window of fixed length len(s1) because two strings are permutations
#  exactly when every letter has the same count (a set would lose counts: 'aab' and 'abb'). Each step one
#  letter enters and one leaves, and I delete a key when its count reaches 0 so the window dict equals
#  s1's dict, and checking every piece of that length once means no possible piece is missed. Time is
#  O(n) and space is O(1), since there are at most 26 letters."
#
# Interview sentence (model):
# "I count the letters of s1, then slide a window of the same length over s2, keeping a dict of its letter
#  counts: add the letter that enters, subtract the one that leaves and delete it at zero. If the two
#  dicts are ever equal, return True. Time is O(n) and space is O(1) because there are only 26 letters."

if __name__ == "__main__":
    print(Solution().checkInclusion("abc", "lecabee"))       # True
    print(Solution().checkInclusion("abc", "lecaabee"))      # False
    print(Solution().checkInclusion("ab", "eidbaooo"))       # True
    print(Solution().checkInclusion("ab", "eidboaoo"))       # False
    print(Solution().checkInclusion("abc", "ab"))            # False
    print(Solution().checkInclusion("a", "a"))               # True

# Next: Fri Nov 13: redo Permutation in String from a blank editor in the morning (say complexity and the
# "because" in my own words), then Minimum Window Substring or move on to Stack. Chapter 9 and 10 recalls owed.
