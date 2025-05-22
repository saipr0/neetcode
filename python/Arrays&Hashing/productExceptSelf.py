class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1]
        prior_product = 1
        for i in range(1, len(nums)):
            prior_product *=nums[i-1]
            res.append(prior_product)

        post_product = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= post_product
            post_product *= nums[i]

        return res




# Test
s = Solution()
print(s.productExceptSelf([1,2,3,4]))
