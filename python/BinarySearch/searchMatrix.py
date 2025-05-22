class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n - 1

        while l<=r:
            mid = l + (r-l)//2
            if matrix[(mid//n)][(mid%n)] < target:
                l = mid+1
            elif matrix[(mid//n)][(mid%n)] > target:
                r = mid-1
            else:
                return True
        return False


# Test
s = Solution()
print(s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
print(s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))
print(s.searchMatrix(matrix = [[1],[3]], target = 1))
