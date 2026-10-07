# python_practice17.py  --  Oct 7, 2026
# Problem: Group Anagrams (NeetCode 150, new problem)
# Status: Accepted, 47/47 test cases (152ms, 14.1 MB)

from typing import List

# ---------------------------------------------------------------
# 1. Restate
# Given a list of words, group together the words that are anagrams
# of each other. Order of groups and order inside groups don't matter.
#
# 2. Brute force
# Compare every word against every other word with an anagram check.
# 1,000 words -> about 500,000 comparisons. O(n^2).
# Doubling the words quadruples the work.
#
# 3. Bottleneck
# We compare PAIRS of words. We want each word to land in its group
# on its own, without looking at the others.
#
# 4. Tool
# Pattern clue: "group things sharing a property"
#   -> dict with the shared property as the key.
# Shared property = the signature (the word's letters, sorted).
#   "eat", "tea", "ate"  ->  all sort to "aet"
# Key = signature, value = LIST of words with that signature.
#
# 5. Steps
#   a. make an empty dict
#   b. for each word, compute its signature (sort the letters)
#   c. key already exists -> append the word to its list
#      key is new         -> create the key with a one-item list
#   d. return only the values (the lists), signatures dropped
# ---------------------------------------------------------------


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            key = ''.join(sorted(word))      # sorted("eat") -> ['a','e','t'] -> "aet"
            if key in groups:
                groups[key].append(word)     # NO "=" : append changes the list in place
            else:
                groups[key] = [word]         # new key starts with a LIST holding the word
        return list(groups.values())


# ---------------------------------------------------------------
# Trace on ["eat", "tea", "tan", "ate", "nat", "bat"]
#
# word   key    key in groups?   groups after
# "eat"  aet    no               {"aet": ["eat"]}
# "tea"  aet    yes              {"aet": ["eat", "tea"]}
# "tan"  ant    no               {"aet": ["eat", "tea"], "ant": ["tan"]}
# "ate"  aet    yes              {"aet": ["eat", "tea", "ate"], "ant": ["tan"]}
# "nat"  ant    yes              {"aet": ["eat", "tea", "ate"], "ant": ["tan", "nat"]}
# "bat"  abt    no               {..., "abt": ["bat"]}
#
# list(groups.values()) -> [["eat","tea","ate"], ["tan","nat"], ["bat"]]
# ---------------------------------------------------------------

# Bugs I made and fixed today (remember these):
#   1. groups[key] = groups[key].append(word)
#      .append returns None, so the "=" overwrote the list with None.
#      Fix: groups[key].append(word)   (no "=")
#   2. groups[key] = word
#      Stored a plain string. Next .append on it would crash.
#      Fix: groups[key] = [word]       (a list)
#   3. Test lines: call through the class -> Solution().groupAnagrams(strs)

# Complexity:
#   Brute force: O(n^2)   every word compared with every other word
#   Dict + signature: about O(n)   each word handled ONE time
#   (plus a small cost to sort each short word)

# Interview sentence:
# "I used a dict with the sorted letters as the key, because all anagrams
#  share the same signature, so each word goes straight into its group
#  without being compared to the others."

# Pattern table addition:
#   "Group things sharing a property" -> dict, shared property is the key,
#   value is a list.

if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))
    # Expected: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

# Next: Thursday Oct 8 = Valid Anagram, dict-loop version (no Counter),
# from a BLANK editor. Group Anagrams returns about 2 weeks later.
