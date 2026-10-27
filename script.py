def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in pairs.values():
            stack.append(char)
        if char in pairs:
            if stack or stack[-1] == char:
                


print(is_valid("()")   )  # True
print(is_valid("([])")  ) # True
print(is_valid("([)]") )  # False
print(is_valid("(((")  )  # False
print(is_valid("}{")   )  # False