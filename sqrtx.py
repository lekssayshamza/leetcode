# Link: https://leetcode.com/problems/sqrtx/description/

# def mySqrt(x):
#     i = 0
#     nums = [0]
#     while nums[i] < x:
#         i += 1
#         nums.append(i*i)

#     return i if x == nums[i] else i - 1 

def mySqrt(x):
    left = 0
    right = x

    while left <= right:
        mid = (left + right) // 2
        mid_pwr = mid * mid

        if x < mid_pwr:
            right = mid - 1
        elif x > mid_pwr:
            left = mid + 1
        else:
            return mid

    return right

    
x = 25
print(mySqrt(x))