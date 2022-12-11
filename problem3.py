# Time Complexity: O(n)
# Space Complexity: max O(n), not count the result space
# where n is the length of str

class Solution:

    def returnValidParentheses(self, str):

        res = self.removeInvalidClosing(str, '(', ')')
        res = self.removeInvalidClosing(res[::-1], ')', '(')
        return res[::-1]

    def removeInvalidClosing(self, str, opening, closing):
        stack = []
        balance = 0

        for s in str:
            if s == opening:
                balance += 1
            elif s == closing:
                if balance <= 0:
                    continue
                else:
                    balance -= 1
            stack.append(s)

        return ''.join(stack)



print(Solution().returnValidParentheses("lee(t(c)o)de)"))
print(Solution().returnValidParentheses("a)b(c)d"))
print(Solution().returnValidParentheses("))(("))
print(Solution().returnValidParentheses("(inf)o6(20(5)"))
print(Solution().returnValidParentheses("("))
print(Solution().returnValidParentheses("al(go(r)))ithm(s("))
