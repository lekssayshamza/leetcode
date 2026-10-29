def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    mid = len(nums) // 2

    while (left <= right):
        mid = (left + right) // 2
        if target > nums[mid]:
            left = mid + 1
            # mid += ((right - left + 1) // 2 + 1)
            # mid = (right - left) // 2 + left
        elif target < nums[mid]:
            right = mid - 1
            # mid -= ((right - left + 1) // 2 + 1)
            # mid = (right - left) // 2 + left
        else:
            return mid

    return -1


nums = [4, 9, 15, 22, 31, 46, 58]

print(binary_search(nums, 31))  # 4
print(binary_search(nums, 4))   # 0
print(binary_search(nums, 58))  # 6
print(binary_search(nums, 20))  # -1
print(binary_search([], 10))    # -1