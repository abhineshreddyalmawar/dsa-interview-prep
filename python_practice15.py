# DAY 3 (Aug 12, 2026) | NeetCode: Group Anagrams
# Hardest solo problem yet - combines dict grouping + sorted() + .join() + .append()

# --- key insight: sorted() gives an IDENTICAL result for any anagram ---
# sorted("eat") == sorted("tea") == ['a', 'e', 't']  -- proven, this is what makes grouping possible

# --- .join() : converts a sorted LIST back into a STRING, usable as a dict key ---
# (lists can't be dict keys - only strings/numbers/tuples can)
key_example = "".join(sorted("eat"))
print(key_example)   # "aet"

# --- Group Anagrams : dict where key = sorted signature, value = growing list of matching words ---
def groupAnagrams(strs):
    groups = {}
    for word in strs:
        key = "".join(sorted(word))       # identical for all anagrams of this word
        if key in groups:
            groups[key].append(word)       # same group seen before -> add to existing list
        else:
            groups[key] = [word]            # first time seeing this pattern -> start a new list
    return list(groups.values())            # .values() = just the groups, drop the sorted keys

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

# solo re-derivation, cold, on a new input - reproduced correctly from memory
print(groupAnagrams(["abc", "bca", "xyz", "cab"]))
# [['abc', 'bca', 'cab'], ['xyz']]

# NOTE: System Design continues next session - today's full time went to this problem