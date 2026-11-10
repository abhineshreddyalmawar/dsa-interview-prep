# python_practice37.py  --  Nov 10, 2026 (Tuesday, week 2 of the new routine: 4 new problems a week)
# Problem: Longest Repeating Character Replacement (new problem; sliding window with a dict of counts;
#          taught from the idea up, then written by me)
# Results: morning Accepted 39/39, 46 ms (beats 98.50%), memory 8.2 MB (beats 77.59%).
#          evening redo from a blank editor, no comments: Accepted 39/39, 46 ms (beats 98.50%),
#          memory 8.2 MB (beats 77.59%).

# ---------------------------------------------------------------
# The six questions
#   1. Name:    Longest Repeating Character Replacement
#   2. Does:    finds the length of the longest connected stretch that can be made of ONE single letter
#               by changing at most k of its letters (to any capital letter)
#   3. Input:   a string s of capital letters, and a number k (the changes allowed)
#   4. Output:  one number: that longest length, e.g. s = "XYYX", k = 2 -> 4 (YYYY);
#               s = "AABABBA", k = 1 -> 4 (AAAA)
#   5. Steps every time: say it in one sentence; name input and output with a tiny example;
#      ask "what do I need to remember?"; pick the tool; stage comments, then code;
#      trace a tricky input; say time and space; derive the "because" from the trace.
#   6. Algorithm (the five jobs):
#        1. PREPARE    -> counts = {} (letter -> its count inside the window), left = 0, best = 0
#        2. GO THROUGH -> for right in range(len(s)): right walks one letter at a time
#        3. UPDATE     -> add the new letter to counts: first time 1, otherwise + 1
#        4. DECIDE     -> while (right - left + 1) - max(counts.values()) > k: the window needs more
#                         changes than allowed (changes needed = length - count of the most common letter)
#        5. SHRINK     -> inside the while: counts[s[left]] = counts[s[left]] - 1, THEN left = left + 1
#        6. UPDATE     -> the window is valid: length = right - left + 1; if length > best: best = length
#        7. RETURN     -> return best, after the loop
#
# Key question: what must I remember? How many times each letter appears in the window (a count attached
# to each letter, so a dict), where the window's two fingers are (left, right), and the best length so far.
#   "longest stretch of one letter / change at most k letters" -> a dict of counts plus a window
#   (left and right) and a best number: sliding window.
# ---------------------------------------------------------------


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        best = 0
        left = 0
        for right in range(len(s)):
            if s[right] in counts:
                counts[s[right]] = counts[s[right]] + 1
            else:
                counts[s[right]] = 1
            while ((right - left + 1) - max(counts.values())) > k:
                counts[s[left]] = counts[s[left]] - 1
                left = left + 1
            length = right - left + 1
            if length > best:
                best = length
        return best


# Trace for s = "XYYX", k = 1 (positions 0 to 3: X Y Y X):
#   right 0 (X): counts {X: 1}        length 1, max 1, needs 0; 0 > 1 is False          best 1
#   right 1 (Y): counts {X: 1, Y: 1}  length 2, max 1, needs 1; 1 > 1 is False          best 2
#   right 2 (Y): counts {X: 1, Y: 2}  length 3, max 2, needs 1; 1 > 1 is False          best 3
#   right 3 (X): counts {X: 2, Y: 2}  length 4, max 2, needs 2; 2 > 1 is True -> shrink:
#                counts[s[0]] = X goes 2 -> 1, left = 1; check again: window "YYX", length 3, max 2,
#                needs 1; 1 > 1 is False -> stop; length 3, 3 > 3 is False                  best 3
#   return 3
#   Same string with k = 2: the while never runs (the whole string needs only 2 changes), left stays 0,
#   X goes 1 -> 1 -> 1 -> 2; the answer is 4.
#   Smallest input s = "A", k = 0: counts {A: 1}; needs 0, 0 > 0 is False; length 1 > 0, best 1 -> return 1
#
# Slips fixed today:
#   1. Unsure what the problem meant: after at most k changes the stretch must be ONE single letter
#      (e.g. YYYY); the replacement letter can be any capital letter, but the best choice is the letter
#      that already appears most in the stretch.
#   2. Found the rule on my own: changes needed = length - count of the most common letter; a window is
#      valid when that is AT MOST k (<= k), not "matches k".
#   3. for right in len(s) needs range(...) and a colon.
#   4. Worked out the window formula once before the while, so the while could never finish (an infinite
#      loop): the formula must be recalculated each time, so it goes inside the while condition.
#   5. The count-down line: counts[s[left]] = counts[s[left]] - 1 (the key is the letter at the left
#      finger, the sign is minus); the dict must always describe the window; it goes BEFORE left moves,
#      or s[left] would point to the next letter.
#   6. Thought left moves every round: left moves only inside the while; with k = 2 on "XYYX" the while
#      never runs, with k = 1 it runs once, at right = 3.
#   7. Asked why the while stops at 1 > 1: it keeps going while the condition is True and stops the first
#      time it is False; needing 1 change when 1 is allowed is fine (strictly more than k shrinks).
#   8. Hand-trace of "A" with k = 0: the answer is 1 (the best update 1 > 0 runs), not 0.
#   9. Space: O(1), not O(n) as yesterday, because the dict holds at most 26 capital letters; time O(n).
#   10. Redo slip: the else line stored counts[right] (a position) instead of counts[s[right]] (a letter),
#       the position-vs-value slip again; found by tracing the first rounds.
#   11. The "because" needed the reason skipping is safe: any longer stretch that starts earlier and ends
#       at the same right contains the too-wide window, and adding letters can never reduce the changes
#       needed.
#
# Complexity: time O(n): right walks the string once and left only moves forward, so each letter enters
#               the window once and leaves at most once; max(counts.values()) looks at at most 26
#               counts, a fixed cost (about 26 times n, which is O(n)).
#             space O(1): the dict holds at most 26 capital letters, however long the string is; left,
#               right, best and length are single numbers.
#
# I used X because Y:
# "I used a dict of counts with a window (left and right) and a best number because a window is valid
#  when its length minus its most common count is at most k. When it is not, I move left forward one
#  step at a time until it is valid, and I never need to check the stretches I skipped, because any
#  longer stretch ending at the same right contains the too-wide window and can only need the same or
#  more changes. Time is O(n) and space is O(1), since the dict holds at most 26 letters."
#
# Interview sentence:
# "I keep a window with a left and a right pointer and a dict of letter counts. The window needs its
#  length minus its most common count changes, so while that is more than k I shrink it from the left,
#  reducing the count of the letter that leaves; then I update the best length. Time is O(n) and space is
#  O(1) because there are only 26 letters."

if __name__ == "__main__":
    print(Solution().characterReplacement("XYYX", 2))        # 4
    print(Solution().characterReplacement("XYYX", 1))        # 3
    print(Solution().characterReplacement("AABABBA", 1))     # 4
    print(Solution().characterReplacement("AAABABB", 1))     # 5
    print(Solution().characterReplacement("A", 0))           # 1
    print(Solution().characterReplacement("AAAA", 0))        # 4
    print(Solution().characterReplacement("ABCD", 0))        # 1

# Next: Wed Nov 11: the next sliding window problem (Permutation in String), then the evening redo and quiz.
