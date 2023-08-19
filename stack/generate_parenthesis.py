class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = ["()"]
        s = set()

        for i in range(1, n):
            for e in result:
                for j in range(len(e)//2-1, len(e)):
                    s.add(e[:j] + "()" + e[j:])
            result = list(s)
            s.clear()

        return result