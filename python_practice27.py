# python_practice27.py  --  Oct 23, 2026 (Friday, repeats from a blank editor)
# Problems: Product of Array Except Self (repeat), Valid Palindrome (repeat)
# Results: Product of Array Except Self Accepted 51/51, 91 ms (beats 98.51%), 9.9 MB (beats 97.14%).
#          Valid Palindrome Accepted 43/43, 27 ms (beats 94.93%), 7.7 MB (beats 99.52%).
# Stage comments written by me first; one small slip each, fixed from a hint.

from typing import List

# ---------------------------------------------------------------
# Product of Array Except Self (repeat)
# PLAN
#   1. result = [1] * len(nums)   -> n slots to write into (a position must exist before result[i] = ...)
#   2. left = 1                   -> running product of everything to the LEFT
#   3. for i in range(len(nums)): result[i] = left ; left = left * nums[i]   (use first, then update)
#   4. right = 1                  -> running product of everything to the RIGHT
#   5. for i in range(len(nums) - 1, -1, -1): result[i] = result[i] * right ; right = right * nums[i]
#      (backwards, because right is built from the last position: nothing is on its right, so it is 1,
#       and each step multiplies in the number that is now on the right)
#   6. return result              -> lined up with the first 'for'
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


# Slip fixed today: the range had four numbers (len(nums)-1, -1, -1, -1); range takes three:
#   start = len(nums) - 1 (last position), stop = -1 (so 0 is included), step = -1.
# Complexity: time O(n): two loops one after the other, each visits every number once.
#             space O(1) extra, not counting the returned list (only left, right, i).
#             (O(n) if you count the output list.)


# ---------------------------------------------------------------
# Valid Palindrome (repeat)
# PLAN
#   1. cleaned = []
#   2. for char in s: if char.isalnum(): cleaned.append(char.lower())   (lowercase too)
#   3. left = 0 ; right = len(cleaned) - 1
#   4. while left < right: if cleaned[left] != cleaned[right]: return False
#   5.   left + 1 ; right - 1   (inside the while, level with the if, not under it)
#   6. return True              -> lined up with the 'while'
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


# Slip fixed today: left = 1 skipped the first character (the first pair is positions 0 and last),
#   so "Was it a car or a cat I saw?" would have printed False. A hand trace of the first pair catches it.
#   In the plan: the name was len(nums) (previous problem) instead of len(cleaned), and the
#   lowercase step was missing in the first draft of the comments.
# Complexity: time O(n); space O(n) for the cleaned list.

if __name__ == "__main__":
    print(ProductExceptSelf().productExceptSelf([1, 2, 3, 4]))        # [24, 12, 8, 6]
    print(ProductExceptSelf().productExceptSelf([2, 3]))              # [3, 2]
    print(ProductExceptSelf().productExceptSelf([1, 0, 3]))           # [0, 3, 0]
    print(ValidPalindrome().isPalindrome("Was it a car or a cat I saw?"))   # True
    print(ValidPalindrome().isPalindrome("tab a cat"))                      # False
    print(ValidPalindrome().isPalindrome(" "))                              # True

# Next: Mon Oct 26: three new problems for the week (Two Sum II, then the next two), each repeated in the same week.
