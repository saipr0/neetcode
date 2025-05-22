from collections import defaultdict

class Solution:
    def groupAnagram(self, strs: list[str]) -> list[list[str]]:
        myhash = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1
            myhash[tuple(count)].append(s)

        return list(myhash.values())


# Test
s = Solution()
print(s.groupAnagram(["eat","tea","tan","ate","nat","bat"]))
# print(s.groupAnagram([1,2,3,4]))

