# python_practice25.py  --  Oct 21, 2026 (Wednesday, new problem)
# Problem: Product of Array Except Self (NeetCode 150, Arrays & Hashing)
# Result: Accepted 51/51. Runtime 92 ms (beats 98.52%), memory 9.9 MB (beats 97.13%).
# Built from a stage-comment skeleton; slips fixed from hints.

from typing import List

# ---------------------------------------------------------------
# PLAN (stage comments, what to write and why)
#   1. result = [1] * len(nums)   -> answers list; 1 is safe (an empty side multiplies by 1)
#   2. left = 1                   -> running product of everything to the LEFT
#   3. for i in range(len(nums)):  result[i] = left ; then left = left * nums[i]
#                                  (use first, then update)
#   4. right = 1                  -> running product of everything to the RIGHT
#   5. for i in range(len(nums) - 1, -1, -1):  (last position down to 0)
#        result[i] = result[i] * right ; then right = right * nums[i]
#   6. return result              -> lined up with the first 'for'
#
# Idea: answer at position i = (product of numbers left of i) x (product of numbers right of i).
# ---------------------------------------------------------------


class Solution:
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


# ---------------------------------------------------------------
# Slips and lessons today:
#   1. The empty side of the split is 1, not 0 (multiplying by 1 changes nothing).
#   2. I looped over values before; here I need positions: for i in range(len(nums)),
#      then nums[i] is the value and i is the position.
#   3. [1] * len(nums) makes a list of 1s; [1 * len(nums)] is a one-item list.
#   4. The loop variable must match the body (i, not position).
#   5. range(start, stop, step) takes three numbers. Backwards: range(len(nums) - 1, -1, -1).
#      len(nums) closes before the "- 1".
#   6. Use first, then update: result[i] uses the running product BEFORE nums[i] is included.
#   7. Run the code and read the error line: NameError and TypeError name the problem.
#
# Trace for [1, 2, 4, 6]:
#   after loop 1: result = [1, 1, 2, 8]
#   loop 2 (right): i=3 -> 8*1=8, right=6; i=2 -> 2*6=12, right=24;
#                   i=1 -> 1*24=24, right=48; i=0 -> 1*48=48.  Final [48, 24, 12, 8]
#
# Complexity: time O(n): two loops one after the other, each visits every number once.
#             space O(1) extra, not counting the returned list (only left, right, i).
#
# Interview sentence:
# "Each answer is the product of everything to its left times everything to its right.
#  I fill the left products in one pass and multiply in the right products in a second pass,
#  so it is O(n) time with O(1) extra space, without using division."
# ---------------------------------------------------------------

if __name__ == "__main__":
    print(Solution().productExceptSelf([1, 2, 3, 4]))      # [24, 12, 8, 6]
    print(Solution().productExceptSelf([1, 2, 4, 6]))      # [48, 24, 12, 8]
    print(Solution().productExceptSelf([2, 3]))            # [3, 2]
    print(Solution().productExceptSelf([1, 0, 3]))         # [0, 3, 0]
    print(Solution().productExceptSelf([-1, 0, 1, 2, 3]))  # [0, -6, 0, 0, 0]

# Next: repeat Product of Array Except Self on Fri Oct 23 from a blank editor,
# writing the 6 stage comments first, then the code. New problem tomorrow: Valid Palindrome.
