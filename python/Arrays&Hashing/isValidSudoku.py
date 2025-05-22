from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rowh = defaultdict(set)
        colh = defaultdict(set)
        boxh = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                
                if (board[i][j] in rowh[i] or
                    board[i][j] in colh[j] or
                    board[i][j] in boxh[((i//3),(j//3))]):
                        return False

                rowh[i].add(board[i][j])
                colh[j].add(board[i][j])
                boxh[((i//3),(j//3))].add(board[i][j])
        return True




# Test
s = Solution()
print(s.isValidSudoku(board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

print(s.isValidSudoku(board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
