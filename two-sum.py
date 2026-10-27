# link https://leetcode.com/problems/two-sum/description/

def twoSum(nums, target):
    needed = {}

    for i in range(len(nums)):
        comp = target - nums[i]
        if nums[i] in needed:
            return [needed[nums[i]], i]
        
        needed[comp] = i



nums = [3,3]
target = 6
print(twoSum(nums, target))


"""
needed = {
                7: 1

             }

             
num: 7

comp: 7

"""