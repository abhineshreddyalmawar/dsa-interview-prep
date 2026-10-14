# python_practice22.py  --  Oct 14, 2026 (Wednesday, new problem)
# Problem: Longest Consecutive Sequence (NeetCode 150, Arrays & Hashing)
# Result: Accepted 34/34. Runtime 81 ms (beats 24.44%), memory 22.8 MB (beats 36.50%).
# First write used the stage-comment skeleton. Four bugs in the first draft, all fixed from hints.

from typing import List

# ---------------------------------------------------------------
# PLAN (stage comments, what to write and why)
#   1. BUILD:        Build = set(nums)        -> one-step "is it there?" lookups
#   2. BEST:         Best = 0                 -> the answer; 0 also covers an empty list
#   3. LOOP:         for number in nums
#   4. START CHECK:  if number - 1 not in Build   -> only the FIRST number of a chain counts
#   5. COUNT:        current = number, length = 1
#                    while current + 1 in Build: current + 1, length + 1
#   6. UPDATE:       if length > Best: Best = length   (after the while, inside the start block)
#   7. RETURN:       return Best, lined up with the 'for'
#
# One sentence: put the numbers in a set, find each chain's first number,
# count upward from it, keep the longest.
# ---------------------------------------------------------------


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Build = set(nums)
        Best = 0
        for number in nums:
            key = number - 1
            if key not in Build:
                current = number
                length = 1
                while current + 1 in Build:
                    current = current + 1
                    length = length + 1
                if length > Best:
                    Best = length
        return Best


# ---------------------------------------------------------------
# Bugs and lessons today:
#   1. Build = set() made an EMPTY set. It has to be filled: set(nums).
#   2. Start check was backwards: 'in' means the number has something before it
#      (skip it). The chain start is 'not in'.
#   3. current[number] / length[number]: plain numbers cannot be indexed.
#      Same mistake as counts[number] on Top K. Just current + 1, length + 1.
#   4. The 'if length > Best' update was under 'else' and 'length' did not exist
#      there. It belongs right after the while loop, inside the start block.
#   5. The while loop stops when current + 1 is NOT in the set (chain ended),
#      not when the input runs out.
#   6. Why skip numbers that have a number before them: they are in the middle of
#      a chain; counting from them repeats work done from the chain's first number.
#
# Complexity: time O(n). The set is built in O(n); each number is walked over only
# once in total (only chain starts count upward), so the loops are O(n) together.
# Space O(n) for the set.
# (List instead of set would make each lookup O(n) and the whole thing O(n^2).)
#
# Interview sentence (30 seconds, to say in my own words):
# "I put the numbers in a set so each lookup takes one step. I start counting only
#  at a number with nothing before it, count upward while the next number is in the
#  set, and keep the longest chain. Each number is counted once, so it is linear
#  time, at the cost of extra memory for the set."
# ---------------------------------------------------------------

if __name__ == "__main__":
    print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))        # 4
    print(Solution().longestConsecutive([]))                            # 0
    print(Solution().longestConsecutive([5]))                           # 1
    print(Solution().longestConsecutive([1, 1, 1]))                     # 1
    print(Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
    print(Solution().longestConsecutive([-2, -1, 0, 5]))                # 3

# Next: repeat Longest Consecutive Sequence on Fri Oct 16 from a blank editor,
# writing the 7 stage comments first, then the code.
