class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height)-1
        max_area = 0
        
        while l<r:
            min_ind = l if height[l] < height[r] else r
            max_area = max(max_area, height[min_ind] * (r-l))
            
            if min_ind == l: l+=1
            else: r-=1

        return max_area

# Test
s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
