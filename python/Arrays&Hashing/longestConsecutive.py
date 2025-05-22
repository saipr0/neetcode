class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0
        for n in num_set:
            if n-1 in num_set: continue
            count = 1
            while n+1 in num_set:
                count += 1
                n+=1
            longest = max(longest, count)
        return longest


# Test
s = Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))
