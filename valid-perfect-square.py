# Link: https://leetcode.com/problems/valid-perfect-square/description/

def isPerfectSquare(num):
    left = 0
    right = num

    while(left <= right):
        mid = (left + right) // 2
        mid_squared = mid * mid

        if num > mid_squared:
            left = mid + 1
        elif num < mid_squared:
            right = mid - 1
        else:
            return True

    return False




print(isPerfectSquare(14))