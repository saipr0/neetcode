class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        return True



# Test
s = Solution()
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
print(s.containsDuplicate([1,2,3,4]))

