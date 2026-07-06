class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack = []
        for tok in tokens:
            if tok == '+':
                self.stack.append(self.stack.pop()+self.stack.pop())
            elif tok == '*':
                self.stack.append(self.stack.pop()*self.stack.pop())
            elif tok == '-':
                sec = self.stack.pop()
                first = self.stack.pop()
                self.stack.append(first-sec)
            elif tok == '/':
                sec = self.stack.pop()
                first = self.stack.pop()
                self.stack.append(int(float(first)/sec))
            else:
                self.stack.append(int(tok))
        return self.stack[0]