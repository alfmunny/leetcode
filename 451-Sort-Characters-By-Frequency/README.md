# 451 - Sort Characters By Frequency

[leetcode](https://leetcode.com/problems/sort-characters-by-frequency/)

## Problem

    Given a string, sort it in decreasing order based on the frequency of characters.
    
    Example 1:
    
    Input:
    "tree"
    
    Output:
    "eert"
    
    Explanation:
    'e' appears twice while 'r' and 't' both appear once.
    So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
    
    Example 2:
    
    Input:
    "cccaaa"
    
    Output:
    "cccaaa"
    
    Explanation:
    Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
    Note that "cacaca" is incorrect, as the same characters must be together.
    
    Example 3:
    
    Input:
    "Aabb"
    
    Output:
    "bbAa"
    
    Explanation:
    "bbaA" is also a valid answer, but "Aabb" is incorrect.
    Note that 'A' and 'a' are treated as two different characters.

## Solution

1.  Use a map to count the characters.
2.  Loop the map to the characters into a map using the frequency as key. The value will be a list, containing all the characters with the same frequency.
3.  Go through the map.

### Solution 1: Two maps

```python
from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = defaultdict(int)
        freq = {}
        max_f = 0
        ans = ""

        for c in s:
            cnt[c] += 1

        for c, f in cnt.items():
            if f not in freq:
                freq[f] = []

            freq[f].append(c)
            max_f = max(max_f, f)

        for i in range(max_f, 0, -1):
            if i in freq:
                for c in freq[i]:
                    ans += c * i

        return ans
```

### Solution 2: One liner

```python
from collections import Counter
class Solution:
    def frequencySort(self, s):
        return "".join([c * cnt for c, cnt in Counter(s).most_common()])
```
