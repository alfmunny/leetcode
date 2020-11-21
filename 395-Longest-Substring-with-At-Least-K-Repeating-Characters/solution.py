class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        c = Counter(s)
        for i, v in c.items():
            if v < k:
                return max(self.longestSubstring(x, k) for x in s.split(i))
        return len(s)
