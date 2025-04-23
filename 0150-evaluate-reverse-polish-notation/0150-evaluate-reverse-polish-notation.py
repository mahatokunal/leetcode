class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ('+', '-', '*', '/'):
                b = stack.pop()
                a = stack.pop()
                stack.append(self.performOp(a,b,token))
            else:
                stack.append(int(token))
        return stack[0]
    def performOp(self,a,b,token):
        if token == '+':
            return a+b
        elif token == '-':
            return a-b
        elif token == '*':
            return a*b
        else:
            return int(a/b)