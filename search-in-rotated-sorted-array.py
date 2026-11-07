# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/description

def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] > target and target < nums[right]:
            left = mid + 1
        else:
            right = mid 


nums = [4,5,6,7,0,1,2]
target = 0

print(search(nums, target))