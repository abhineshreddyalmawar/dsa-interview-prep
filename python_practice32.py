# python_practice32.py  --  Nov 2, 2026 (Monday, week 1 of the new routine: 4 new problems a week)
# Problem: Two Sum II (new problem; guessed the notebook with a hint, then rebuilt from a blank editor in the evening)
# Results: morning Accepted 76/76, 77 ms (beats 99.97%), memory 11.2 MB (beats 79.40%).
#          evening redo Accepted 76/76, 137 ms (beats 22.42%; same algorithm, the runtime varies run to run),
#          memory 11.1 MB (beats 99.62%).

from typing import List

# ---------------------------------------------------------------
# The six questions
#   1. Name:    Two Sum II (input array is sorted)
#   2. Does:    finds the two numbers that add up to the target and returns their positions,
#               counted from 1 (not 0); the list is sorted; exactly one answer exists;
#               the solution must use only O(1) extra space
#   3. Input:   a sorted list of whole numbers (numbers) and a whole number (target)
#   4. Output:  a list of two positions, counted from 1, e.g. [1, 2]
#   5. Steps every time: say it in one sentence; name input and output with a tiny example;
#      ask "what do I need to remember?"; pick the tool; stage comments, then code;
#      trace the smallest input; say time and space.
#   6. Algorithm (the five jobs):
#        1. PREPARE    -> left = 0, right = len(numbers) - 1   two single numbers, outside the loop
#        2. GO THROUGH -> while left < right
#        3. DECIDE     -> total = numbers[left] + numbers[right]
#                         equal to the target: return [left + 1, right + 1]  (+1 because positions start at 1)
#        4. UPDATE     -> too big: right = right - 1 (a smaller number on the right)
#                         too small: left = left + 1 (a bigger number on the left)
#        5. RETURN     -> nothing after the loop: exactly one answer is guaranteed
#
# Key question: what must I remember? Only where my two fingers are: two positions, single numbers.
# Why not a dict (Two Sum)? The problem demands O(1) extra space, and a dict stores up to n numbers.
# Why it works: the list is SORTED. Moving left forward gives a bigger number, moving right back gives
# a smaller one, so the sum tells me which finger to move.
#   "sorted + O(1) extra space + two numbers that add up" -> two pointers.
# ---------------------------------------------------------------


class TwoSumII:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            elif total > target:
                right = right - 1
            else:
                left = left + 1


# Trace for [1, 2, 3, 4], target 3 (indexes and numbers kept separate):
#   round 1: left 0, right 3: 1 + 4 = 5 > 3  -> right = 2
#   round 2: left 0, right 2: 1 + 3 = 4 > 3  -> right = 1
#   round 3: left 0, right 1: 1 + 2 = 3 == 3 -> return [0 + 1, 1 + 1] = [1, 2]
#   right: 3 -> 2 -> 1 (an index, not the number 4).
#   Also: [2, 7, 11, 15], target 9: left 0, right 1 gives 2 + 7 = 9 -> [1, 2]; the returned values are
#   positions, not the numbers (2 and 7).
#
# Slips fixed today:
#   1. Reached for a dict (Two Sum) first; sorted plus O(1) extra space means two pointers.
#   2. Tried moving left forward when the sum was too big; testing by hand showed it makes the sum bigger
#      (7 + 15 = 22), while moving right back makes it smaller (2 + 11 = 13).
#   3. left[nums[i]] is not valid: left is a single number; "the number at position left" is numbers[left].
#   4. = stores a value, == asks "is it equal?".
#   5. Python spells it elif, and the last case is just else: with no condition.
#   6. The sum line goes on its own line under the while, and the if/elif/else go inside the loop.
#   7. The parameter is numbers (not nums); do not name a variable sum (a built-in): use total.
#   8. Trace comments mixed up values and indexes (right=4-1=3); write right: 3, 2, 1.
#
# Complexity: time O(n): each round moves one finger inward, so the fingers meet after at most n
#               rounds, and each round is one addition and one comparison (O(1)).
#             space O(1): only left, right and total are stored, single numbers.
#
# I used X because Y:
# "I used two pointers because the list is sorted: a sum that is too big means the right number must get
#  smaller, so I move right back, and a sum that is too small means I move left forward. That needs no
#  dict, so the extra space stays O(1)."
#
# Interview sentence:
# "Because the list is sorted, I put one pointer at each end and add the two numbers. If the sum is too
#  big I move the right pointer back, if it is too small I move the left pointer forward, and when it
#  matches I return the positions plus one. Time is O(n) and space is O(1)."

if __name__ == "__main__":
    print(TwoSumII().twoSum([1, 2, 3, 4], 3))      # [1, 2]
    print(TwoSumII().twoSum([2, 7, 11, 15], 9))    # [1, 2]
    print(TwoSumII().twoSum([1, 3, 4, 5], 8))      # [2, 4]
    print(TwoSumII().twoSum([-1, 0], -1))          # [1, 2]

# Next: Tue Nov 3: Container With Most Water (two pointers), then the evening redo and quiz.
