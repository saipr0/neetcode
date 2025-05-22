class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        val_to_index = {}
        
        for i, n in enumerate(nums):
            val_to_index[n] = i

        for i, n in enumerate(nums):
            if target-n in val_to_index and val_to_index[target-n] != i:
                return [i, val_to_index[target-n]]


# Test
s = Solution()
print(s.twoSum(nums = [2,7,11,15], target = 9))
# print(s.twoSum([1,2,3,4]))

