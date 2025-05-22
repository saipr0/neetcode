class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 1
        while l<=r:
            mid = l + (r-l)//2

            t = 0
            for i in piles:
                if i % mid == 0:
                    t += i//mid
                else:
                    t += i//mid + 1

            if t > h:
                l = mid + 1
            else:
                res = mid
                r = mid - 1

        return res


# Test
s = Solution()
print(s.minEatingSpeed(piles = [3,6,7,11], h = 8))
print(s.minEatingSpeed(piles = [30,11,23,4,20], h = 5))
print(s.minEatingSpeed(piles = [30,11,23,4,20], h = 6))
