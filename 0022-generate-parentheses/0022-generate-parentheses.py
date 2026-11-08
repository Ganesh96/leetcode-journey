class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        combinations = []

        def dfs(parenthesis, open_count, close_count):

            if open_count == n and close_count == n:
                combinations.append(parenthesis)
                return

            if open_count < n:
                dfs(
                    parenthesis + "(",
                    open_count + 1,
                    close_count
                )

            if close_count < open_count:
                dfs(
                    parenthesis + ")",
                    open_count,
                    close_count + 1
                )

        dfs("", 0, 0)

        return combinations