from collections import defaultdict

class Solution:
    def findAllAnagrams(self, s, p):
        target, window = defaultdict(int), defaultdict(int)
        left, right = 0, 0
        match = 0
        ans = []

        for c in p:
            target[c] += 1

        while right < len(s):
            c = s[right]
            if c in target:
                window[c] += 1
                if window[c] == target[c]:
                    match += 1

            right += 1

            while right - left + 1 > len(p):
                if match == len(target):
                    ans.append(left)
                c = s[left]
                left += 1

                if c in window:
                    if window[c] == target[c]:
                        match -= 1
                    window[c] -= 1


        return ans

print(Solution().findAllAnagrams("cbaeabac", "abc"))
