# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[right]


nums = [11,13,15,17]    

print(findMin(nums))