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
print(Solution().frequencySort("treeaaaaaaa"))
