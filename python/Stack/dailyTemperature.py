class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        res = [0]*len(temperatures)

        for i in range(len(temperatures)):
            if not stack:
                stack.append([i, temperatures[i]])
            while stack and stack[-1][1] < temperatures[i]:
                ind, temp = stack.pop()
                res[ind] = i - ind
            stack.append([i, temperatures[i]])

        return res


# Test
s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))
