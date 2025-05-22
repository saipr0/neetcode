class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {} # val -> occurrence
        for n in nums:
            count[n] = count.get(n, 0) + 1

        freq = [[] for i in range(len(nums))]
        for n in count:
            freq[count[n]-1].append(n)

        res = []
        for l in range(len(freq)-1, -1, -1):
            if freq[l] is None:
                continue
            for n in freq[l]:
                res.append(n)
                if len(res) == k: 
                    return res


# Test
s = Solution()
print(s.topKFrequent(nums = [1], k = 1))
# print(s.topKFrequent([1,2,3,4]))

