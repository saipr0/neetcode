class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        myhash = {')':'(', '}':'{', ']':'['}

        for b in s:
            if b in myhash.values():
                stack.append(b)
            else:
                if not stack or stack[-1] != myhash[b]:
                    return False
                stack.pop()
        
        return not stack



# Test
s = Solution()
print(s.isValid("()[]{}"))
print(s.isValid("]"))
