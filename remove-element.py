# link: https://leetcode.com/problems/remove-element/description/

def removeElement(nums, val):
    write = 0

    for read in range(len(nums)):
        if nums[read] != val:
            nums[write] = nums[read]
            write += 1

    return write

nums = [3, 2, 5, 5, 2, 7, 8]
val = 2

print(removeElement(nums, val))