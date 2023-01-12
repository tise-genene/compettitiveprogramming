def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    index = 0
    stack = []

    for p in pushed:
        stack.append(p)
        while stack and stack[-1] == popped[index]:
            stack.pop()
            index += 1
            
    return not stack
