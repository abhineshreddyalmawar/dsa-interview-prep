# python_practice34.py  --  Nov 4, 2026 (Wednesday, week 1 of the new routine: 4 new problems a week)
# Problem: 3Sum (new problem; taught from the idea up, then written by me)
# Results: morning Accepted 35/35, 206 ms (beats 35.41%), memory 8.4 MB (beats 100.00%).
#          evening redo from a blank editor, no comments: Accepted 35/35, 181 ms (beats 59.88%),
#          memory 8.2 MB (beats 100.00%).

from typing import List

# ---------------------------------------------------------------
# The six questions
#   1. Name:    3Sum
#   2. Does:    finds every group of THREE numbers (a triplet) that adds up to 0, with no
#               triplet repeated in the answer
#   3. Input:   a list of whole numbers (nums), not sorted
#   4. Output:  a list of triplets: a list of lists, three numbers in each,
#               e.g. [[-1, -1, 2], [-1, 0, 1]]
#   5. Steps every time: say it in one sentence; name input and output with a tiny example;
#      ask "what do I need to remember?"; pick the tool; stage comments, then code;
#      trace the smallest input; say time and space.
#   6. Algorithm (the five jobs):
#        1. PREPARE    -> sort nums; groups = []   (the sorted list lets the pointers decide which
#                         finger to move, and puts equal numbers next to each other)
#        2. GO THROUGH -> for i in range(len(nums)): the first number of a triplet
#                         skip repeats: if i != 0 and nums[i] == nums[i - 1]: continue
#                         inner search = Two Sum II on the rest: left = i + 1, right = the last
#                         position, while left < right
#        3. DECIDE     -> total = nums[i] + nums[left] + nums[right]
#                         too big (total > 0): right = right - 1
#                         too small (total < 0): left = left + 1
#                         zero: a triplet
#        4. UPDATE     -> on zero: groups.append([nums[i], nums[left], nums[right]]),
#                         left = left + 1, then while left < right and nums[left] == nums[left - 1]:
#                         left = left + 1 (skip repeated second numbers)
#        5. RETURN     -> return groups, after the loops
#
# Key question: what must I remember? Which first number I am on (i), where the two fingers are
# (left, right), and the triplets found so far (groups).
#   "three numbers add to a target / no duplicate groups / unsorted" -> sort, then a loop that
#   fixes one number, then two pointers (the Two Sum II idea) inside it.
# 3Sum is Two Sum II inside a loop: the target for the inner pair is minus the first number.
# ---------------------------------------------------------------


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        groups = []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right = right - 1
                elif total < 0:
                    left = left + 1
                else:
                    groups.append([nums[i], nums[left], nums[right]])
                    left = left + 1
                    while left < right and nums[left] == nums[left - 1]:
                        left = left + 1
        return groups


# Trace for [-1, 0, 1, 2, -1, -4], sorted: [-4, -1, -1, 0, 1, 2] (positions 0 to 5):
#   i = 0 (value -4): left 1 (-1), right 5 (2): total -3 too small, left 2
#                     left 2 (-1), right 5 (2): total -3, left 3
#                     left 3 (0),  right 5 (2): total -2, left 4
#                     left 4 (1),  right 5 (2): total -1, left 5; 5 < 5 is False, loop stops
#   i = 1 (value -1): left 2 (-1), right 5 (2): total 0 -> append [-1, -1, 2]; left 3;
#                     skip check: nums[3] = 0 vs nums[2] = -1, not equal
#                     left 3 (0), right 5 (2): total 1 too big, right 4
#                     left 3 (0), right 4 (1): total 0 -> append [-1, 0, 1]; left 4; 4 < 4 False
#   i = 2 (value -1): equals nums[1], skipped (the first -1 already tried every triplet starting with -1)
#   i = 3 (value 0):  left 4 (1), right 5 (2): total 3 too big, right 4; 4 < 4 False
#   i = 4, i = 5:     left starts at 5 and 6, so 5 < 5 and 6 < 5 are False, nothing happens
#   result [[-1, -1, 2], [-1, 0, 1]]
#   Smallest input [0, 0, 0]: i = 0, left 1, right 2: total 0 -> append [0, 0, 0]; left 2; 2 < 2 False;
#   i = 1 and i = 2 are skipped as repeats of 0 (or find nothing) -> [[0, 0, 0]]
#
# Slips fixed today:
#   1. Said "pairs" in the name-the-problem step: the groups are triplets (three numbers), and the
#      output is a list of triplets.
#   2. Matched the inner search to Valid Palindrome instead of Two Sum II (the first instinct was
#      right; the closer match is a sorted list with a target).
#   3. right starts at the last position of the list, not "to the right of i"; left starts at i + 1.
#   4. The repeat check compares nums[i] with nums[i - 1] (the number just before it) and uses
#      continue; it does not change the list.
#   5. = vs ==; 0 (zero), not the letter o; groups.append takes ONE thing, so the three numbers go
#      inside one list: groups.append([a, b, c]), with round brackets for the call and square brackets
#      for the list; return groups (not groups.values() or groups()).
#   6. Trace slips: mixed positions and values (0 + 2 + 4) and forgot the first number nums[i] in the
#      total (it is the sum of THREE numbers).
#   7. Forgot left = left + 1 right after the append: the loop would run forever, appending the same
#      triplet. The step after the append is: move left once, then skip repeats with the while.
#   8. The lines after the append (left = left + 1 and the skip while) belong inside the else block.
#   9. The "because" had the fingers' directions swapped: total too big moves the RIGHT finger back; total
#      too small moves the LEFT finger forward.
#
# Complexity: time O(n squared): the outer loop runs n times and each inner walk takes up to n steps;
#               the sort is O(n log n), which is smaller, so the slowest step wins: O(n squared).
#             space O(1) extra: i, left, right and total are single numbers; groups is the output we
#               must return, so it is not counted as extra.
#
# I used X because Y:
# "I used sorting plus two pointers because sorting lets me move the right finger back when the
#  total is too big and the left finger forward when it is too small, and it puts equal numbers next
#  to each other, so I can skip repeats."
#
# Interview sentence:
# "I sort the list, then fix one number at a time and run a two-pointer search on the rest for the
#  pair that adds up to minus that number. If the total is too big I move the right pointer back, if
#  it is too small I move the left pointer forward, and I skip repeated numbers so no triplet appears
#  twice. Time is O(n squared) and space is O(1) extra."

if __name__ == "__main__":
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))   # [[-1, -1, 2], [-1, 0, 1]]
    print(Solution().threeSum([0, 1, 1]))               # []
    print(Solution().threeSum([0, 0, 0]))               # [[0, 0, 0]]
    print(Solution().threeSum([0, 1, -1]))              # [[-1, 0, 1]]

# Next: Thu Nov 5: Best Time to Buy and Sell Stock (the start of sliding window), then the evening redo and quiz.
