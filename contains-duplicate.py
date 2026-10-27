# link: https://leetcode.com/problems/contains-duplicate/description/

def containDuplicate(num):
    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False




nums = [1,1,1,3,3,4,3,2,4,2]
print(containDuplicate(nums))