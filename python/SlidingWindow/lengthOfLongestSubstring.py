class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniq = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in uniq:
                l = max(uniq[s[r]]+1, l)
            uniq[s[r]] = r
            res = max(res, r-l+1)
        return res

# Test
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring("dvdf"))
