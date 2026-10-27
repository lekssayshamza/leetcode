# link: https://leetcode.com/problems/valid-parentheses/description/

def isValid(s):
    stack = []
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif not stack or stack[-1] != pairs[char]:
            return False
        else:
            stack.pop()

    if stack:
        return False

    return True


s = "([)]"
print(isValid(s))