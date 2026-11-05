# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

def searchRange(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if target <= nums[mid]:
            right = mid
        else:
            left = mid + 1


    if nums and nums[right] == target:
        first = right
        left = first
        right = len(nums)

        while left < right:
            mid = (left + right) // 2

            if target < nums[mid]:
                right = mid
            else:
                left = mid + 1

        return [first, right - 1]


    return [-1, -1]

print(searchRange([5, 7, 7, 8, 8, 8, 10], 8))  # [3, 5]
print(searchRange([5, 7, 8, 8, 8], 8))          # [2, 4]
print(searchRange([8], 8))                      # [0, 0]
print(searchRange([8, 8, 8], 8))                # [0, 2]
print(searchRange([5, 7, 9], 8))                # [-1, -1]
print(searchRange([], 8))                      # [-1, -1]