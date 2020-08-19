# 1079 - Letter Tile Possibilities

[leetcode](https://leetcode.com/problems/letter-tile-possibilities/)

## Problem

    You have n  tiles, where each tile has one letter tiles[i] printed on it.
    
    Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.
    
     
    
    Example 1:
    
    Input: tiles = "AAB"
    Output: 8
    Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
    Example 2:
    
    Input: tiles = "AAABBC"
    Output: 188
    Example 3:
    
    Input: tiles = "V"
    Output: 1
     
    
    Constraints:
    
    1 <= tiles.length <= 7
    tiles consists of uppercase English letters.

## Solution

```python
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.ans = 0
        mark = [False] * len(tiles)
        self.dfs(sorted(tiles), mark)
        return self.ans

    def dfs(self, tiles, mark):
        for i in range(len(tiles)):
            if mark[i] or (i > 0 and tiles[i] == tiles[i-1] and not mark[i-1]):
                continue
            mark[i] = True
            self.ans += 1
            self.dfs(tiles, mark)
            mark[i] = False
```
