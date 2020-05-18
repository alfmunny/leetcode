from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target, window = defaultdict(int), defaultdict(int)
        left, right = 0, 0
        match = 0
        for c in s1:
            target[c] += 1

        while (right < len(s2)):

            c = s2[right]
            if c in target:
                window[c] += 1
                if window[c] == target[c]:
                    match += 1

            right += 1

            while (right - left + 1 > len(s1)):
                if match == len(target):
                    return True
                c = s2[left]
                left += 1

                if c in window:
                    if window[c] == target[c]:
                        match -= 1

                    window[c] -= 1
        return False
