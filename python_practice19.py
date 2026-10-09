# python_practice19.py  --  Oct 9, 2026 (Friday, repeat day)
# Problem: Group Anagrams, from a blank editor (NeetCode 150)
# Repeat of Oct 7. This repeat needed hints (7 bugs on the first attempt).

from typing import List

# ---------------------------------------------------------------
# PLAN
# Key = the word's letters sorted ("eat", "tea", "ate" -> "aet").
# Value = a LIST of the words that share that key.
# Steps:
#   1. make an empty dict
#   2. for each word, compute its key
#   3. key exists -> append the word to that list
#      key is new -> create it with a one-item list [word]
#   4. return list(groups.values())
# ---------------------------------------------------------------


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        return list(groups.values())


# ---------------------------------------------------------------
# Bugs I made today (4 of them are repeats of the same few ideas):
#   1. Signature: a type hint uses ":" not "="   ->   strs: List[str]
#      (copy NeetCode's line, don't type it from memory)
#   2. "".join.sorted(word)  ->  "".join(sorted(word))
#      sorted(...) is CALLED with the word; join TAKES its result.
#   3. Typo: gorups  ->  groups
#   4. .append[word]  ->  .append(word)   calls use ( ), not [ ]
#   5. groups[key] = word  ->  groups[key] = [word]     (REPEAT BUG from Oct 7)
#      The VALUE must be a LIST, because later I call .append on it.
#      A plain word has no .append.
#      (list(...) at the end is separate: it turns groups.values()
#       into a list of those lists.)
#   6. return groups.values  ->  return list(groups.values())
#   7. Test: Solution() with a capital S; ONE list argument in [ ].
#
# Complexity: about O(n). Each word is handled ONCE and goes straight
# to its group, with no comparing against the other words.
# (Sorting each short word adds a small cost.)
#
# Interview sentence:
# "I used a dict where the key is the word's letters sorted, because all
#  anagrams share the same sorted key. For each word I either append it to
#  the existing list for that key or start a new list, and at the end I
#  return the dict's values, which are the groups."
# ---------------------------------------------------------------

if __name__ == "__main__":
    print(Solution().groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
    # Expected: [['act', 'cat'], ['pots', 'tops', 'stop'], ['hat']]

# Next: Group Anagrams returns about 2 weeks later (resurface Oct 17 / Oct 24).
