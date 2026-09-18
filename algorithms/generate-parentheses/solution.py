class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        path = []

        def backtrack(open, close):

            # Complete valid combination
            if open == n and close == n:
                result.append("".join(path))
                return

            # Choice 1: add '('
            if open < n:
                path.append("(")
                backtrack(open + 1, close)
                path.pop()          # BACKTRACK

            # Choice 2: add ')'
            if close < open:
                path.append(")")
                backtrack(open, close + 1)
                path.pop()          # BACKTRACK

        backtrack(0, 0)

        return result