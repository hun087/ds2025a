# print(1+2))
def is_valid_parentheses(expression : str) -> bool: # type hint   bool - return type, str - parameter data type
    stack = list()
    for letter in expression:
        if letter == "(":
            stack.append(letter)
        if letter == ")":
            if len(stack) == 0:
                return  False   # )1+2(), (1+2))
            else:
                stack.pop()
    return len(stack) == 0  # (1+2), ((3*2)/2), ((3*2/2)

print(is_valid_parentheses(")1+2()"))   # if len(stack) == 0: return  False 에 걸림
print(is_valid_parentheses("(1+2))"))   # ""안 마지막 ) 에서 걸림
print(is_valid_parentheses("(1+2)"))    # push 1번 pop 1번 - stack == 0
print(is_valid_parentheses("((3*2)/2)"))    # push 2번 pop 2번 - stack == 0
print(is_valid_parentheses("((3*2/2)")) # len(stack) - False (여는 괄호 더 많을때)