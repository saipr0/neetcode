from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        l = r = 0
        q = deque()

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r+1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res



# Test
s = Solution()
print(s.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
print(s.maxSlidingWindow(nums = [1], k = 1))
