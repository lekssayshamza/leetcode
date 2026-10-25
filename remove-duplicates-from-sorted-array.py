# link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

def removeDuplicates(nums):
    write = 0

    for read in range(1, len(nums)):
        if nums[read] != nums[write]:
            write += 1
            nums[write] = nums[read]

    if not nums:
        k = 0
    else:
        k = write + 1
    return k
    

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))
