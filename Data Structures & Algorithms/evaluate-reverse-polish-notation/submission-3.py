class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        operations = set("+-*/")
        while len(tokens) > 0:
            token = tokens.pop(0)
            if token in operations:
                op2 = nums.pop() # right number for operation
                op1 = nums.pop() # left number for operation
                
                if token == '+':
                    nums.append(op1+op2)
                elif token == '-':
                    nums.append(op1 - op2)
                elif token == '*':
                    nums.append(op1*op2)
                elif token == '/':
                    nums.append(int(op1/op2))
                #print(f"{op1}{token}{op2}={nums[-1]}")
            else:
                nums.append(int(token))
        return nums[0]