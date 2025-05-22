class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def addBracket(s: str, openb: int, closeb: int):
            if openb == closeb == 0 :
                res.append(''.join(s))
                return 

            if openb > 0:
                s.append('(')
                addBracket(s, openb-1, closeb)
                s.pop()

            if closeb > openb:
                s.append(')')
                addBracket(s, openb, closeb-1)
                s.pop()

        addBracket([], n, n)
        return res

# Test
s = Solution()
print(s.generateParenthesis(3))
