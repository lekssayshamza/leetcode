# link: https://leetcode.com/problems/search-insert-position/description/

def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1

    while (left <= right):
        mid = (left + right) // 2

        if (target > nums[mid]):
            left = mid + 1
        elif (target < nums[mid]):
            right = mid - 1
        else:
            return mid

    return left


nums = [1,3,5,6]
target = 7

print(searchInsert(nums, target))