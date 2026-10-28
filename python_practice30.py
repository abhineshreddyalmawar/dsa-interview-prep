# python_practice30.py  --  Oct 28, 2026 (Wednesday, revision week day 3)
# Problems: Longest Consecutive Sequence (taught again from the idea up, then rebuilt by me)
#           Group Anagrams (bonus, planned for Fri; built the same way, guessing the notebook first)
# Results: Longest Consecutive Sequence Accepted 34/34, 108 ms (beats 5.46%), memory 22.5 MB (beats 36.37%).
#          Group Anagrams Accepted 47/47, 142 ms (beats 67.49%), memory 14.2 MB (beats 88.11%).

from typing import List

# ---------------------------------------------------------------
# The six questions
#   1. Name:    Longest Consecutive Sequence
#   2. Does:    finds the longest chain of numbers that follow each other by one (1, 2, 3, 4)
#               in an unsorted list, and returns its length
#   3. Input:   an unsorted list of whole numbers (nums)
#   4. Output:  one whole number, the length of the longest chain; must be O(n)
#   5. Steps every time: say it in one sentence; name input and output with a tiny example;
#      ask "what do I need to remember?"; pick the tool; stage comments, then code;
#      trace the smallest input (an empty list!); say time and space.
#   6. Algorithm (the five jobs):
#        1. PREPARE    -> build = set(nums)   once, before the loop: a yes/no lookup in one step
#                         best = 0            longest so far; 0 also covers an empty list
#        2. GO THROUGH -> for number in nums
#        3. DECIDE     -> behind = number - 1; if behind not in build:   the START check:
#                         only a number with nothing just below it starts a chain
#        4. UPDATE     -> inside the start block: current = number; length = 1;
#                         while current + 1 in build: current = current + 1; length = length + 1
#                         after the while, still inside the start block: if length > best: best = length
#        5. RETURN     -> return best, after the loop, lined up with the 'for'
#
# Key question: what must I remember about each number? Only a yes/no: "is the next number
# (or the one below) in there?" Nothing is attached -> a set (a list would scan: O(n) per question).
#   "consecutive / chain / O(n)" -> set plus a start check.
# ---------------------------------------------------------------


class LongestConsecutive:
    def longestConsecutive(self, nums: List[int]) -> int:
        build = set(nums)
        best = 0
        for number in nums:
            behind = number - 1
            if behind not in build:
                current = number
                length = 1
                while current + 1 in build:
                    current = current + 1
                    length = length + 1
                if length > best:
                    best = length
        return best


# Trace for [100, 4, 200, 1, 3, 2]:
#   starts (nothing just below): 100 (99 missing), 200 (199 missing), 1 (0 missing)
#   walk from 100: 101 missing -> length 1
#   walk from 200: 201 missing -> length 1
#   walk from 1: 2, 3, 4 are there, 5 is missing -> length 4
#   best = 4
#
# How "not in" works: 'x not in s' is True when x is missing. An 'if' runs its block only on True.
#   So 'if behind not in build' runs for a start. With {1, 2, 3, 4}: only 1 is a start
#   (0 is missing); 2 is not (1 is there); 3 is not (2 is there).
#
# Slips fixed today:
#   1. UnboundLocalError: 'current' was used in the 'while' without being assigned on that path.
#      current = number must run before the while, in the same block.
#   2. The while checked 'current + 1 in nums' (the LIST, a scan each time). It must be the set.
#   3. 'return best' was indented inside the for loop, so an empty list returned None (the loop
#      never ran) and a non-empty list returned after the first number. It lines up with the 'for'.
#   4. Mixed up the output (a count) with what the notebook remembers (a yes/no). The notebook
#      is about the question asked for each number, not about the final answer.
#   5. Said "one step, O(n)". One step is O(1); the loop is O(n) because it does n of them.
#   6. Called 2 and 3 starts in [1, 2, 3, 4]. A start has NOTHING just below it: only 1.
#
# Complexity: time O(n): the for loop visits each number once, and because of the start check each
#               chain is walked only from its start, so all the while walks together touch each
#               number about once: n + n = 2n, drop the constant. Without the start check, walking
#               from every number would revisit numbers: O(n^2).
#             space O(n): the set holds up to n numbers; current, length and best are single
#               numbers (O(1)).
#
# I used X because Y:
# "I used a set because 'is the next number there?' is a yes/no lookup that takes one step
#  (O(1)). I only start walking at a number with nothing just below it, so each chain is
#  walked once and the total is O(n)."
#
# Interview sentence:
# "I put the numbers in a set, then for each number with no number just below it, I walk up the
#  chain counting its length and keep the best. The start check means each number is walked once,
#  so time is O(n) and space is O(n)."

# ---------------------------------------------------------------
# Group Anagrams (bonus)
#   1. Name:   Group Anagrams
#   2. Does:   puts the words that are anagrams of each other into the same group
#   3. Input:  a list of words (strs)
#   4. Output: a list of groups, each group a list of words (a list of lists), any order
#   Key question: what must I remember? Which words share the same letters.
#   What is the same for all anagrams? The SORTED letters ("eat", "tea", "ate" all give "aet").
#   So the label (key) is the sorted letters, and the value is a LIST of the words with that
#   label -> a dict whose values are lists.
#   "group items that share a property" -> dict with list values.
#   The five jobs:
#     1. PREPARE    -> groups = {}   key = sorted letters, value = list of words
#     2. GO THROUGH -> for word in strs
#     3. DECIDE     -> key = "".join(sorted(word)); if key in groups
#     4. UPDATE     -> key already there: groups[key].append(word)
#                      key new:           groups[key] = [word]   (a list holding the first word)
#     5. RETURN     -> return list(groups.values())   after the loop, lined up with the 'for'
#   Python fact: sorted("eat") gives a LIST of letters, and a list cannot be a dict key,
#   so join the letters back into a string: "".join(sorted("eat")) gives "aet".
# ---------------------------------------------------------------


class GroupAnagrams:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        return list(groups.values())


# Trace for ["act", "pots", "tops", "cat"]:
#   "act":  key "act", new          -> groups = {"act": ["act"]}
#   "pots": key "opst", new         -> groups = {"act": ["act"], "opst": ["pots"]}
#   "tops": key "opst", already     -> groups["opst"] = ["pots", "tops"]
#   "cat":  key "act", already      -> groups["act"] = ["act", "cat"]
#   return the values: [["act", "cat"], ["pots", "tops"]]
#
# Slips fixed today:
#   1. The loop name and the body must match: "for words in strs" with "sorted(word)" is a NameError.
#   2. The parameter is strs, not str.
#   3. Wrote groups.append(word): a dict has no .append. The LIST under the key has it:
#      groups[key].append(word).
#   4. Wrote groups[key] = word. The value must be a list, so a new key stores [word].
#   5. list(groups.values) needs the parentheses to run it: list(groups.values()).
#   6. The empty string is two quote marks: "".join(...).
#
# Complexity: time O(n x k log k): the loop runs n times (n words), and each round sorts one word
#               of k letters, which costs k log k; the dict check and append are O(1).
#             space O(n x k): the dict stores all n words of up to k letters, and the keys add
#               more letters.
#
# I used X because Y:
# "I used a dict whose values are lists, with the sorted letters as the key, because the sorted
#  letters are the same for every anagram, so the key groups the words, and the value must hold
#  several words, so it is a list."
#
# Interview sentence:
# "I sort the letters of each word to make a key that is the same for all its anagrams, and I keep
#  a dict from that key to the list of words. Time is O(n x k log k) because of the sorting, and
#  space is O(n x k)."

if __name__ == "__main__":
    print(LongestConsecutive().longestConsecutive([100, 4, 200, 1, 3, 2]))        # 4
    print(LongestConsecutive().longestConsecutive([]))                            # 0
    print(LongestConsecutive().longestConsecutive([1, 1, 1]))                     # 1
    print(LongestConsecutive().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
    print(LongestConsecutive().longestConsecutive([2, 20, 4, 10, 3, 4, 5]))       # 4
    print(GroupAnagrams().groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
    # [['act', 'cat'], ['pots', 'tops', 'stop'], ['hat']]
    print(GroupAnagrams().groupAnagrams(["x"]))                                    # [['x']]
    print(GroupAnagrams().groupAnagrams([""]))                                     # [['']]

# Next: Thu Oct 29: Product of Array Except Self (left and right running products), and Valid Palindrome
# if energy allows. Fri: revision day. Sat: the Saturday check and the pace decision.
