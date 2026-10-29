# python_practice31.py  --  Oct 29, 2026 (Thursday, revision week day 4)
# Problems: Product of Array Except Self (taught again from the idea up, then rebuilt by me)
#           Valid Palindrome (bonus; two pointers, guessed the notebook first)
# Results: Product of Array Except Self Accepted 51/51, 157 ms (beats 24.19%), memory 9.9 MB (beats 97.19%).
#          Valid Palindrome Accepted 43/43, 27 ms (beats 94.87%), memory 7.7 MB (beats 99.53%).

from typing import List

# ---------------------------------------------------------------
# The six questions
#   1. Name:    Product of Array Except Self
#   2. Does:    for every position, multiplies all the OTHER numbers (not the one at that position)
#   3. Input:   a list of whole numbers (nums)
#   4. Output:  a list of the same length; answer[i] = product of every number except nums[i]
#               (no division allowed; must be O(n))
#   5. Steps every time: say it in one sentence; name input and output with a tiny example;
#      ask "what do I need to remember?"; pick the tool; stage comments, then code;
#      trace the smallest input; say time and space.
#   6. Algorithm (the five jobs):
#        1. PREPARE    -> result = [1] * len(nums)   one answer slot per position, starting at 1
#                         left = 1                    running product of everything to the LEFT
#        2. GO THROUGH -> pass 1: for i in range(len(nums))
#        3. DECIDE     -> no choice here: every position gets its left product
#        4. UPDATE     -> result[i] = left  (USE first), then left = left * nums[i]  (UPDATE after)
#                         pass 2: right = 1, for i in range(len(nums) - 1, -1, -1)  (backwards)
#                         result[i] = result[i] * right, then right = right * nums[i]
#        5. RETURN     -> return result, after both loops
#
# Key question: what must I remember? One answer per position (a list, indexed by position)
# plus two single running numbers. The empty side of the first/last position is 1, because
# multiplying by 1 changes nothing.
#   "product of all except self / no division" -> list plus left and right running products.
# ---------------------------------------------------------------


class ProductExceptSelf:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        left = 1
        for i in range(len(nums)):
            result[i] = left
            left = left * nums[i]
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * right
            right = right * nums[i]
        return result


# Trace for [1, 2, 4, 6]:
#   pass 1 (use left, then update it):
#     i=0: result[0] = 1,  left = 1*1 = 1
#     i=1: result[1] = 1,  left = 1*2 = 2
#     i=2: result[2] = 2,  left = 2*4 = 8
#     i=3: result[3] = 8,  left = 8*6 = 48       result = [1, 1, 2, 8]
#   pass 2 (backwards, use right, then update it), right starts at 1:
#     i=3: result[3] = 8*1  = 8,   right = 1*6  = 6
#     i=2: result[2] = 2*6  = 12,  right = 6*4  = 24
#     i=1: result[1] = 1*24 = 24,  right = 24*2 = 48
#     i=0: result[0] = 1*48 = 48,  right = 48*1 = 48
#   result = [48, 24, 12, 8]
#   (the first value of left and of right is just the starting 1: nothing is multiplied yet)
#
# Slips fixed today:
#   1. Dict first by reflex; the notebook is a list: one answer per position, found by index.
#   2. The trace comments mixed up the values left AFTER the update with the values stored in
#      result BEFORE the update. Use first, then update: result after pass 1 is [1, 1, 2, 8].
#   3. Wrote "1*0" as the first running value; nothing is multiplied for the first one, it is
#      just the starting 1 (the empty side).
#   4. Said space was O(1) because result is O(1). result is O(n), but it is the OUTPUT we must
#      return, so it is not counted as extra. Extra space is left, right and i: O(1).
#
# Complexity: time O(n): two loops one after the other, each visits every number once (n + n = 2n,
#               drop the constant), and each step inside is O(1).
#             space O(1) extra: left, right and i are single numbers; result is O(n) but it is the
#               output we must return, so it is not counted.
#
# I used X because Y:
# "I used a list [1] * len(nums) filled in two passes, plus two running numbers, left and right,
#  because the answer at each position is the product of everything to its left times everything
#  to its right. I avoided dividing the total product, because a zero in the list would break the
#  division."
# One liner for the list: "every position needs its own answer, and a list lets me store and update
#  it by index, result[i]."
#
# Interview sentence:
# "For each position, the answer is the product of everything on its left times everything on its
#  right. I fill a result list with the left products going forward, then multiply in the right
#  products going backward, each with one running number. Time is O(n), and space is O(1) extra
#  because the result is the output."

# ---------------------------------------------------------------
# Valid Palindrome (bonus)
#   1. Name:   Valid Palindrome
#   2. Does:   checks whether a string reads the same forwards and backwards, ignoring capital
#              letters and anything that is not a letter or a number
#   3. Input:  a string (s)
#   4. Output: True or False
#   Key question: what must I remember? Where my two fingers are: two positions, single numbers.
#   "reads the same from both ends / match from the outside in" -> two pointers.
#   The five jobs (two phases):
#     Phase A, clean:
#       1. PREPARE    -> cleaned = []
#       2. GO THROUGH -> for char in s
#       3. DECIDE     -> if char.isalnum()   (letter or number; everything else is skipped)
#       4. UPDATE     -> cleaned.append(char.lower())
#     Phase B, compare:
#       1. PREPARE    -> left = 0, right = len(cleaned) - 1   (AFTER Phase A, so the length is known)
#       2. GO THROUGH -> while left < right   (stop when the fingers meet or cross)
#       3. DECIDE     -> if cleaned[left] != cleaned[right]: return False
#       4. UPDATE     -> left = left + 1, right = right - 1   (they matched: move both inward)
#       5. RETURN     -> return True, after the while, lined up with the while
# ---------------------------------------------------------------


class ValidPalindrome:
    def isPalindrome(self, s: str) -> bool:
        cleaned = []
        for char in s:
            if char.isalnum():
                cleaned.append(char.lower())
        left = 0
        right = len(cleaned) - 1
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left = left + 1
            right = right - 1
        return True


# Trace for "abba" (cleaned = [a, b, b, a]):
#   round 1: left 0, right 3: a == a -> move: left 1, right 2
#   round 2: left 1, right 2: b == b -> move: left 2, right 1
#   2 < 1 is False, so the loop stops -> return True
#   Smallest inputs: "" gives cleaned = [], right = -1, 0 < -1 is False -> True.
#                    "a" gives left 0, right 0, 0 < 0 is False -> True.
#
# Slips fixed today:
#   1. Guessed a set at first. A set is "have I seen this?"; here the notebook is two single
#      numbers, left and right (positions), plus the cleaned list.
#   2. The tool is char.isalnum() (not .alnum()), and lowercase is char.lower() (not .lower(char)).
#   3. A letter is kept AND lowercased: if it is alphanumeric, append its lowercase; otherwise skip.
#   4. A test call "isPalindrome(["tab a cat"])" had square brackets (a list); a string is
#      isPalindrome("tab a cat").
#   5. Wording: "2 < 1 is False, so the loop stops" (the condition fails).
#   6. The "because" repeated the list reason and left out the two-pointers reason.
#
# Complexity: time O(n): two loops one after the other: the for loop visits all n characters, the
#               while loop at most n/2 (the fingers walk toward each other); n + n/2, drop the
#               constants; each step inside is O(1).
#             space O(n): the cleaned list can hold up to n characters in the worst case
#               (a string of only letters and numbers). left and right are O(1).
#
# I used X because Y:
# "I used a list because the order of the characters matters, so I can look at cleaned[left] and
#  cleaned[right]. I used two pointers because I compare pairs from the outside in and stop at the
#  first pair that differs, so I never build a reversed copy."
#
# Interview sentence:
# "I clean the string into a list of lowercase letters and numbers, then I put one pointer at each
#  end and compare the pair, moving inward, and return False at the first mismatch. Time is O(n) and
#  space is O(n)."
#
# Interview follow-up to be ready for: "Can you do it in O(1) space?" Yes: skip the cleaning list,
# move left up while it points at a non-alphanumeric character, move right down likewise, then
# compare the lowercase characters. That is the two-pointer version without the extra list.

if __name__ == "__main__":
    print(ProductExceptSelf().productExceptSelf([1, 2, 4, 6]))        # [48, 24, 12, 8]
    print(ProductExceptSelf().productExceptSelf([-1, 0, 1, 2, 3]))    # [0, -6, 0, 0, 0]
    print(ProductExceptSelf().productExceptSelf([5]))                 # [1]
    print(ValidPalindrome().isPalindrome("Was it a car or a cat I saw?"))  # True
    print(ValidPalindrome().isPalindrome("tab a cat"))                # False
    print(ValidPalindrome().isPalindrome(""))                         # True
    print(ValidPalindrome().isPalindrome("a"))                        # True

# Next: Fri Oct 30: revision day (lighter, class night). Sat Oct 31: the Saturday check and the pace
# decision (5 new problems a week with same-day evening redo, or 4 first, then 5).
