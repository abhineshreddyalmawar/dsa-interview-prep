# python_practice29.py  --  Oct 27, 2026 (Tuesday, revision week day 2)
# Problems: Two Sum (taught again from the idea up, then rebuilt by me)
#           Top K Frequent Elements (bonus, planned for Wed; built the same way, guessing the notebook first)
# Results: Two Sum Accepted 33/33, 27 ms (beats 100%), memory 8 MB (beats 49.64%).
#          Top K Frequent Accepted 99/99, 156 ms (beats 95.28%), memory 13.7 MB (beats 100%).

from typing import List

# ---------------------------------------------------------------
# The six questions
#   1. Name:    Two Sum
#   2. Does:    finds the two numbers that add up to the target and returns their POSITIONS
#   3. Input:   a list of whole numbers (nums) and a whole number (target)
#   4. Output:  a list of two positions, e.g. [0, 1]; exactly one answer exists
#   5. Steps every time: say it in one sentence; name input and output with a tiny example;
#      ask "what do I need to remember?"; pick the tool; stage comments, then code;
#      trace the smallest input; say time and space.
#   6. Algorithm (the five jobs):
#        1. PREPARE    -> seen = {}   notebook, empty, once, before the loop
#                         key = a number I passed, value = its position
#        2. GO THROUGH -> for i in range(len(nums))   (I need the position as well)
#        3. DECIDE     -> partner = target - nums[i]; if partner in seen: return
#                         [seen[partner], i]   (partner's position first, then the current one)
#        4. UPDATE     -> else: seen[nums[i]] = i   (store AFTER the check, number -> position)
#        5. RETURN     -> nothing after the loop: exactly one answer is guaranteed
#
# Key question: what must I remember about each number I pass?
#   Its POSITION, because the answer is positions, and I look it up by the number.
#   A set only says yes or no, so it cannot give the position back: dict {number: position}.
#   "find the partner / return positions" -> dict.
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


# Trace for nums = [3, 4, 5, 6], target = 7:
#   i=0: num 3, partner 4, 4 not in seen -> seen = {3: 0}
#   i=1: num 4, partner 3, 3 IS in seen  -> return [seen[3], 1] = [0, 1]
#
# Slips fixed today:
#   1. Reached for a set first ("have I seen it?"), but the answer needs the position,
#      so the notebook is a dict. (Look at my own return line: seen[partner].)
#   2. The check searches for the PARTNER, not the current number: if partner in seen.
#   3. Wrote seen.add(...) (set way). A dict is assigned: seen[nums[i]] = i.
#   4. Wrote seen[partner] = nums[i], which stores the wrong way round. The key is the
#      NUMBER and the value is its position: after i=0 the dict is {3: 0}, not {4: 3}.
#   5. With "for i in range(len(nums))" the current number is nums[i]; there is no "num".
#   6. Comment said dict={4:0}; the trace gives {3:0}. A comment must match the trace.
#
# Complexity: time O(n): the loop runs once for every number, and each round is cheap because
#               'partner in seen' and the store are dict steps (O(1)). With a list, the 'in'
#               would scan and cost O(n) per round.
#             space O(n): the dict can hold up to n numbers. The early exit is the best case;
#               Big O describes the worst case, where the pair is found at the end.
#
# I used X because Y:
# "I used a dict, {number: position}, because the answer needs a position attached to each
#  number, so I can look up the partner by its number in one step."
#
# Interview sentence:
# "For each number I compute its partner, target minus the number. If the partner is already in my
#  dict I return its position and the current position; otherwise I store the number with its
#  position. Time is O(n), space is O(n)."

# ---------------------------------------------------------------
# Top K Frequent Elements (bonus)
#   1. Name:   Top K Frequent Elements
#   2. Does:   returns the k numbers that appear most often
#   3. Input:  a list of whole numbers (nums) and a whole number (k)
#   4. Output: a list of k numbers (order does not matter)
#   Key question: what must I remember about each number? How many times it appears.
#   A number attached to each one -> dict {number: count}. "most frequent" -> counts first.
#   The five jobs:
#     1. PREPARE    -> build = {}  (counts), later result = []
#     2. GO THROUGH -> for num in nums
#     3. DECIDE     -> if num in build
#     4. UPDATE     -> yes: build[num] + 1; no: build[num] = 1
#        then ORDER: ordered = sorted(build.items(), key=lambda pair: pair[1], reverse=True)
#        (a dict is not in count order, and slicing needs an ordered list)
#        then TAKE: for pair in ordered[:k]: result.append(pair[0])   (numbers only, not counts)
#     5. RETURN     -> return result, after the loop, lined up with the for
# ---------------------------------------------------------------


class TopK:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        build = {}
        for num in nums:
            if num in build:
                build[num] = build[num] + 1
            else:
                build[num] = 1
        ordered = sorted(build.items(), key=lambda pair: pair[1], reverse=True)
        result = []
        for pair in ordered[:k]:
            result.append(pair[0])
        return result


# Trace for [1, 2, 2, 3, 3, 3], k = 2:
#   build = {1: 1, 2: 2, 3: 3}
#   ordered = [(3, 3), (2, 2), (1, 1)]   biggest count first
#   ordered[:2] = [(3, 3), (2, 2)] -> result = [3, 2]
#
# Slips fixed today:
#   1. The first dict example had {1: 0 ...}: the first time a number is seen is 1, not 0.
#   2. Wanted to slice right after counting. A dict is not in count order, so sort first.
#   3. Punctuation in the sorted line: lambda pair: pair[1] (colon, no comma after lambda),
#      and a comma between each argument of sorted(...).
#   4. The loop body 'pair[0]' alone does nothing; a list needs result.append(pair[0]).
#   5. [:k] keeps the first k; [k:] skips them.
#   6. A trace comment must show what the loop really sees: ordered[:k], not all of ordered.
#
# Complexity: time O(n log n): counting is O(n) (each dict step O(1)), sorting is O(n log n),
#               the slice loop is O(k); the slowest step wins. Without the sort it would be O(n).
#             space O(n): the build dict and the ordered list both grow with the input
#               (up to n different numbers); result holds only k numbers.
#
# I used X because Y:
# "I used a dict of counts because each number needs a count attached. I sorted the pairs by
#  count because a dict is not in count order, and I sliced the first k because the top k are
#  the first k of the ordered list."
#
# Interview sentence:
# "I count how often each number appears in a dict, sort the pairs by count with the biggest
#  first, and take the first k numbers. Time is O(n log n) because of the sort, space is O(n)."

if __name__ == "__main__":
    print(TwoSum().twoSum([3, 4, 5, 6], 7))   # [0, 1]
    print(TwoSum().twoSum([4, 5, 6], 10))     # [0, 2]
    print(TwoSum().twoSum([3, 3], 6))         # [0, 1]
    print(TopK().topKFrequent([1, 2, 2, 3, 3, 3], 2))   # [3, 2]
    print(TopK().topKFrequent([7, 7], 1))               # [7]

# Next: Wed Oct 28: Longest Consecutive Sequence (Top K was done today as a bonus), after a 10-minute cold redo
# of Two Sum and Top K. Tonight: cold redo of Contains Duplicate and Valid Anagram (10 minutes each).

