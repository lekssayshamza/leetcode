# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

def searchRange(nums, target):
    left = 0
    right = len(nums) - 1

    while (left <= right):
        mid = (left + right) // 2

        


nums = [5,7,7,8,8,10]
target = 8

print(searchRange(nums, target))