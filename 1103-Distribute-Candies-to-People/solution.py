class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        i = 1
        ans = [0] * num_people
        while candies >= 0:
            ans[(i-1) % num_people] += min(candies, i)
            candies -= i
            i += 1
        return ans
