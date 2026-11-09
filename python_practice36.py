# python_practice36.py  --  Nov 9, 2026 (Monday, week 2 of the new routine: 4 new problems a week)
# Problem: Longest Substring Without Repeating Characters (new problem; sliding window with a set;
#          taught from the idea up, then written by me)
# Results: morning Accepted 94/94, 391 ms (beats 32.31%), memory 10.5 MB (beats 94.24%).
#          evening redo from a blank editor, no comments: Accepted 94/94, 367 ms (beats 39.08%),
#          memory 10.7 MB (beats 23.50%).

# ---------------------------------------------------------------
# The six questions
#   1. Name:    Longest Substring Without Repeating Characters
#   2. Does:    finds the length of the LONGEST CONNECTED stretch (substring) of letters with no
#               repeated letter
#   3. Input:   a string s, e.g. "abcabcbb"
#   4. Output:  one number: that longest length, e.g. "abcabcbb" -> 3 ("abc"); "pwwkew" -> 3 ("wke")
#   5. Steps every time: say it in one sentence; name input and output with a tiny example;
#      ask "what do I need to remember?"; pick the tool; stage comments, then code;
#      trace a tricky input; say time and space; derive the "because" from the trace.
#   6. Algorithm (the five jobs):
#        1. PREPARE    -> seen = set() (the letters in the window), left = 0, best = 0
#        2. GO THROUGH -> for right in range(len(s)): right walks one letter at a time
#        3. DECIDE     -> while s[right] is already in seen, the window is not valid
#        4. UPDATE     -> in the while: seen.remove(s[left]), left = left + 1 (letters leave from the
#                         front until the repeat is gone); after the while: seen.add(s[right]);
#                         length = right - left + 1; if length > best: best = length
#        5. RETURN     -> return best, after the loop
#
# Key question: what must I remember? Which letters are in the window (a set), where the window's two
# fingers are (left, right), and the best length so far.
#   "longest stretch / no repeated letter / substring" -> a set plus a window (left and right),
#   sliding window.
# ---------------------------------------------------------------


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        best = 0
        left = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left = left + 1
            seen.add(s[right])
            length = right - left + 1
            if length > best:
                best = length
        return best


# Trace for "zxyxzyx" (positions 0 to 6: z x y x z y x):
#   right 0 (z): not in seen; add; window "z"   length 1, best 1
#   right 1 (x): not in seen; add; window "zx"  length 2, best 2
#   right 2 (y): not in seen; add; window "zxy" length 3, best 3
#   right 3 (x): x is in seen -> remove s[0] = z, left 1; x still in seen -> remove s[1] = x, left 2;
#                x is gone; add x; window "yx" (positions 2 to 3) length 2, best 3
#   right 4 (z): not in seen; add; window "yxz" length 3 (3 > 3 is False), best 3
#   right 5 (y): y in seen -> remove s[2] = y, left 3; add y; window "xzy" length 3, best 3
#   right 6 (x): x in seen -> remove s[3] = x, left 4; add x; window "zyx" length 3, best 3
#   return 3
#   "abba": right 2 (second b) -> remove a (left 1), remove b (left 2); add b; length 1; right 3 (a):
#           the old a was already removed, so no while; add a; length 3 - 2 + 1 = 2; return 2
#   Smallest input "a": the for runs once; "a" is not in seen; add; length 1 > 0, best 1 -> return 1
#   Empty string "": the for never runs -> return 0
#
# Slips fixed today:
#   1. Said the problem was "the number of characters in a string without repetition": it is the
#      LONGEST CONNECTED stretch (substring) with no repeated letter; "abcabcbb" has 8 letters but the
#      answer is 3.
#   2. "pwke" is not allowed for "pwwkew": it skips position 2, and a substring must be connected.
#   3. Said the right finger should stop at a repeat: right never stops; left moves forward, removing
#      letters, until the repeat is gone.
#   4. seen=() makes a tuple; an empty set is set().
#   5. left = 0 and right = 1 were inside the loop (reset every round); left belongs in step 1, and the
#      for already gives right.
#   6. if instead of while (several letters may have to leave); right = right + 1 is not needed with a
#      for; seen.add([right]) should be seen.add(s[right]); there is no else.
#   7. Trace comments were one entry short: left = 1,2,3,4 (four removals), add = z,x,y,z,x,y,z (seven
#      rounds), length = 1,2,3,3,3,3,3.
#   8. Traced "abab" instead of "abba" (voice-typing slip).
#   9. Question: how does a set know which letter to remove? A set removes the VALUE you name; the order
#      comes from the left finger (s[left] is the oldest letter in the window), so letters leave from
#      the front until the repeat is gone. The set and the window must always agree.
#   10. The "because" described WHAT the code does; it must say WHY it works: any stretch starting
#      before the new left would still contain the duplicate, so skipping it loses nothing.
#
# Complexity: time O(n): the right finger walks the string once and left only moves forward; each letter
#               is added to the set once and removed at most once, so there are at most about 2n steps.
#             space O(n): the set holds the letters in the window (up to n different letters, fewer if
#               the alphabet is small); left, right, best and length are single numbers (O(1)).
#
# I used X because Y:
# "I used a set with a window (two fingers) and a best number because when a letter repeats, the
#  window is no longer valid, so I move left forward, removing letters from the set, until the repeated
#  letter is gone. I never need to check the stretches I skipped, because every one of them would still
#  contain the duplicate. Time is O(n) and space is O(n) for the set."
#
# Interview sentence:
# "I keep a window with a left and a right pointer and a set of the letters inside it. For each new
#  letter, if it is already in the set, I move the left pointer forward, removing letters, until the
#  repeat is gone, then I add the letter and update the best length. Time is O(n) and space is O(n)."

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("zxyzxyz"))   # 3
    print(Solution().lengthOfLongestSubstring("xxx"))        # 1
    print(Solution().lengthOfLongestSubstring("abba"))       # 2
    print(Solution().lengthOfLongestSubstring("zxyxzyx"))    # 3
    print(Solution().lengthOfLongestSubstring("a"))          # 1
    print(Solution().lengthOfLongestSubstring(""))           # 0

# Next: Tue Nov 10: the next sliding window problem (Longest Repeating Character Replacement), then the
# evening redo and quiz.
