class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                stack_i, stack_h = stack.pop()
                max_area = max(max_area, stack_h*(i-stack_i))
                start = stack_i

            stack.append([start, h])

        while stack:
            stack_i, stack_h = stack.pop()
            max_area = max(max_area, stack_h*(len(heights)-stack_i))

        return max_area


# Test
s = Solution()
print(s.largestRectangleArea([5,4,1,2]))
