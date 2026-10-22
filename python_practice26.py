# python_practice26.py  --  Oct 22, 2026 (Thursday, new problem and a resurface)
# Problems: Valid Palindrome (new), Two Sum (resurface from an earlier week)
# Results: Valid Palindrome Accepted 43/43, 36 ms (beats 28.93%), memory 7.7 MB (beats 99.52%).
#          Two Sum Accepted 33/33, 31 ms (beats 100%), memory 8 MB (beats 49.04%).
# Both built from stage-comment skeletons; slips fixed from hints.

from typing import List

# ---------------------------------------------------------------
# Valid Palindrome (NeetCode 150, Two Pointers)
# PLAN
#   1. cleaned = []                      -> holds only the characters we keep
#   2. for char in s: if char.isalnum(): cleaned.append(char.lower())
#   3. left = 0 ; right = len(cleaned) - 1   -> pointers at both ends (last position = len - 1)
#   4. while left < right                -> stop when the pointers meet or cross
#   5.   if cleaned[left] != cleaned[right]: return False   (first mismatch decides)
#   6.   left + 1 ; right - 1            -> inside the while, NOT under the if
#   7. return True                       -> lined up with the 'while'
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


# Slips fixed today:
#   1. char.isalnum() is one method name joined by a dot (not "is.alnum").
#   2. cleaned.append(char.lower()): say which list and what to append.
#   3. Indentation: the pointers, the while and return True line up with the for,
#      because they run once, after the cleaning loop. The two moves sit inside the while,
#      at the same level as the if, not under it (else left/right never move on a match).
#   4. Positions start at 0, so the last position is len(cleaned) - 1.
#   5. The while rule left < right: the pointers meet (odd length) or cross (even length);
#      everything has been compared. "abba": (0,3) -> (1,2) -> (2,1) stop.
# Complexity: time O(n): the cleaning loop visits every character, the while about half the list.
#             space O(n): the cleaned list.
#   Later idea: move the pointers over the original string and skip non-alphanumeric characters,
#   which needs only O(1) extra space.
# Interview sentence:
# "I clean the string into lowercase letters and numbers, then two pointers move inward from both
#  ends comparing each pair. The first mismatch returns False; if they meet with no mismatch, True."


# ---------------------------------------------------------------
# Two Sum (repeat, built from a skeleton)
# PLAN
#   1. seen = {}                         -> notebook: key = number passed, value = its position
#   2. for i in range(len(nums))         -> need the position as well as the number
#   3. partner = target - nums[i]
#   4. if partner in seen: return [seen[partner], i]   (partner's position first, then current)
#   5. else: seen[nums[i]] = i           -> store AFTER the check
#   6. nothing after the loop            -> one answer is guaranteed
# ---------------------------------------------------------------


class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            partner = target - nums[i]
            if partner in seen:
                return [seen[partner], i]
            else:
                seen[nums[i]] = i


# Slips fixed today:
#   1. The notebook direction: {number: position}, not {position: number}.
#      A dict is looked up by its KEY, and we search by number.
#   2. When the partner is found, do not add anything: return the answer.
#   3. A dict is assigned (seen[number] = position), not "appended".
#   4. The partner, the check and the store run once per number, so they sit INSIDE the for.
#      Written one level too shallow, they ran once after the loop and returned None.
# Complexity: time O(n): one pass, each dict lookup is one step.
#             space O(n): the dict can hold up to n numbers.

if __name__ == "__main__":
    print(ValidPalindrome().isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(ValidPalindrome().isPalindrome("race a car"))                      # False
    print(ValidPalindrome().isPalindrome(" "))                               # True
    print(ValidPalindrome().isPalindrome("abba"))                            # True
    print(TwoSum().twoSum([3, 4, 5, 6], 7))                                  # [0, 1]
    print(TwoSum().twoSum([4, 5, 6], 10))                                    # [0, 2]
    print(TwoSum().twoSum([3, 3], 6))                                        # [0, 1]

# Next: Fri Oct 23: repeat Product of Array Except Self and Valid Palindrome from a blank editor,
# writing the stage comments first; then the weekly speaking round.
