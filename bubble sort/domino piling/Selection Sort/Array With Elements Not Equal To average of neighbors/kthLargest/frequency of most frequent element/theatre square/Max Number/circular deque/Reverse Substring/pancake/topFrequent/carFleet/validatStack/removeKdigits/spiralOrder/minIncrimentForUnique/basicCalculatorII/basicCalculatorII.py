def calculate(self, s: str) -> int:
    num, operator, stack = 0, '+', []
    opList = ['+', '-', '*', '/']

    for count, i in enumerate(s):
        if i.isnumeric():
            num = num * 10 + int(i)
        if i in opList or count == len(s) - 1:
            if operator == '+':
                stack.append(num)
            elif operator == '-':
                stack.append(-num)
            elif operator == '*':
                j = stack.pop() * num
                stack.append(j)
            elif operator == '/':
                j = int(stack.pop() / num)
                stack.append(j)
        
            operator = i
            num = 0
    
    return sum(stack)
