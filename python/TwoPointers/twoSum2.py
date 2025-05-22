class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers)-1
        while l<r:
            total = numbers[l] + numbers[r]
            if total > target:
                r-=1
            elif total < target:
                l+=1
            else:
                return [l+1, r+1]

# Test
s = Solution()
print(s.twoSum(numbers = [2,7,11,15], target = 9))
print(s.twoSum(numbers = [2,3,4], target = 6))
