# python_practice33.py  --  Nov 3, 2026 (Tuesday, week 1 of the new routine: 4 new problems a week)
# Problem: Container With Most Water (new problem; taught from the idea up, then written by me)
# Result: Accepted 39/39, 64 ms (beats 26.70%), memory 18.6 MB (beats 97.78%).

from typing import List

# ---------------------------------------------------------------
# The six questions
#   1. Name:    Container With Most Water
#   2. Does:    picks two vertical lines as the walls of a container and finds the pair that
#               holds the most water (the water level is the SHORTER wall)
#   3. Input:   a list of heights, one number per line; the position is the spot on the floor
#   4. Output:  one number: the most water any pair can hold
#   5. Steps every time: say it in one sentence; name input and output with a tiny example;
#      ask "what do I need to remember?"; pick the tool; stage comments, then code;
#      trace the smallest input; say time and space.
#   6. Algorithm (the five jobs):
#        1. PREPARE    -> left = 0, right = len(heights) - 1, best = 0   three single numbers
#        2. GO THROUGH -> while left < right
#        3. DECIDE     -> width = right - left
#                         level = min(heights[left], heights[right])   (the shorter wall)
#                         water = level * width
#        4. UPDATE     -> if water > best: best = water
#                         then move the finger on the SHORTER wall one step inward
#                         (if the walls are equal, moving either one is fine)
#        5. RETURN     -> return best, after the loop, lined up with the while
#
# Key question: what must I remember? Where my two fingers are, and the best water so far:
# three single numbers.
#   "pick two positions / best pair / maximise" -> two pointers plus a best number.
# Why move the shorter wall? The shorter wall decides the water level. If I moved the taller
# wall, the level would still be limited by the shorter wall while the width gets smaller, so
# the water could only get smaller. Moving the shorter wall is the only move that can possibly
# raise the level, so every pair I skip could not have beaten the best.
# ---------------------------------------------------------------


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        best = 0
        while left < right:
            width = right - left
            level = min(heights[left], heights[right])
            water = level * width
            if water > best:
                best = water
            if heights[left] < heights[right]:
                left = left + 1
            elif heights[left] > heights[right]:
                right = right - 1
            else:
                left = left + 1
        return best


# Trace for [1, 8, 6, 2, 5, 4, 8, 3, 7] (positions 0 to 8; indexes and values kept apart):
#   round 1: left 0, right 8: width 8, level min(1, 7) = 1, water 8,  best 8;  1 < 7 -> left = 1
#   round 2: left 1, right 8: width 7, level min(8, 7) = 7, water 49, best 49; 8 > 7 -> right = 7
#   round 3: left 1, right 7: width 6, level min(8, 3) = 3, water 18, best 49; 8 > 3 -> right = 6
#   round 4: left 1, right 6: width 5, level min(8, 8) = 8, water 40, best 49; equal  -> left = 2
#   round 5: left 2, right 6: width 4, level min(6, 8) = 6, water 24, best 49; 6 < 8 -> left = 3
#   round 6: left 3, right 6: width 3, level min(2, 8) = 2, water 6,  best 49; left = 4
#   round 7: left 4, right 6: width 2, level min(5, 8) = 5, water 10, best 49; left = 5
#   round 8: left 5, right 6: width 1, level min(4, 8) = 4, water 4,  best 49; left = 6
#   left 6 < right 6 is False, so the loop stops -> return 49
#   Smallest input [1, 1]: left 0, right 1: width 1, level 1, water 1, best 1; equal -> left = 1;
#   1 < 1 is False -> return 1
#
# Slips fixed today:
#   1. Said the water for positions 0 and 8 was 1 * 1: the second number is the WIDTH
#      (8 - 0 = 8), so the water is 1 * 8 = 8, not 1 * 1.
#   2. Width off by one (6 instead of 7 for positions 0 and 7): width = right - left.
#   3. Said the heights could be "the longest ones on either side": the heights come only from
#      the two positions picked, read from the list as heights[left] and heights[right].
#   4. The list is heights (plural); height[left] indexes a single number. Give the shorter wall
#      its own name (level).
#   5. Python spells it elif, with the condition right after it (never "elif:" or "then").
#   6. Updating best and moving a finger are two separate jobs: two separate if blocks, not one
#      long chain.
#   7. right = right - 1 (missing =); the loop body goes on its own lines under the while.
#   8. The "because" described WHAT the code does; it must say WHY it works (why the other pairs
#      can be skipped).
#
# Complexity: time O(n): each round moves one finger inward, so the fingers meet after at most
#               n - 1 rounds, and each round is a few single steps (O(1)).
#             space O(1): only left, right, best (and width, level, water) are stored: single
#               numbers.
#
# I used X because Y:
# "I used two pointers with a best number because moving the shorter wall is the only move that
#  can possibly raise the water level, so I never need to check the other pairs, and it takes
#  n steps instead of checking every pair."
#
# Interview sentence:
# "I put one pointer at each end and work out the water as the shorter wall times the width. I
#  keep the best so far, and I always move the pointer on the shorter wall inward, because moving
#  the taller one can only make the water smaller. Time is O(n) and space is O(1)."

if __name__ == "__main__":
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))   # 49
    print(Solution().maxArea([1, 1]))                        # 1
    print(Solution().maxArea([1, 7, 2, 5, 4, 7, 3, 6]))      # 36

# Next: Wed Nov 4: 3Sum (two pointers on a sorted list), then the evening redo and quiz.
