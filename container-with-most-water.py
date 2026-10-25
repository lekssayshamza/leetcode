# link: https://leetcode.com/problems/container-with-most-water/description

def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = min(height[left], height[right]) * (right - left)

    while right > left:
        if height[right] > height[left]:
            left += 1
        else:
            right -= 1
        max_area = max(max_area, (min(height[left], height[right]) * (right - left)))

    return max_area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(maxArea([1, 1]))
print(maxArea([4, 3, 2, 1, 4]))


"""
l l           r
1 8 6 2 5 4 8 3 7

width = 6
max_area = 49

"""