def is_valid_brackets(expression : str) -> bool: # type hint   bool - return type, str - parameter data type
    stack = list()
    brackets = {']': '[', '}': '{', ')': '('}
    for letter in expression:
        if letter in brackets.values():     # [, {, ( -> brackets.values()
            stack.append(letter)
        if letter in brackets.keys():       # ], }, ) -> brackets.keys()
            if not stack or stack.pop() != brackets[letter]:
                return  False       # stack 남아 있으면 False
    return not stack

print(is_valid_brackets("[({1+2)]}"))
print(is_valid_brackets("[({1+2})]"))
print(is_valid_brackets(")1+2()"))
print(is_valid_brackets("(1+2))"))
print(is_valid_brackets("(1+2)"))
print(is_valid_brackets("((3*2)/2)"))
print(is_valid_brackets("((3*2/2)"))