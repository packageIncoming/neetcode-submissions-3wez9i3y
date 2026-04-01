class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for token in tokens:
            if token == '+':
                op2 = nums.pop() # right number for operation
                op1 = nums.pop() # left number for operation
                nums.append(op1+op2)
            elif token == '-':
                op2 = nums.pop() # right number for operation
                op1 = nums.pop() # left number for operation
                nums.append(op1 - op2)
            elif token == '*':
                op2 = nums.pop() # right number for operation
                op1 = nums.pop() # left number for operation
                nums.append(op1*op2)
            elif token == '/':
                op2 = nums.pop() # right number for operation
                op1 = nums.pop() # left number for operation
                nums.append(int(op1/op2))
            else:
                nums.append(int(token))
        return nums[0]