# link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

def twoSum(numbers, target):
    left = 0
    right = len(numbers) -  1

    while right > left:
        current_sum = numbers[right] + numbers[left]
        if current_sum > target:
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            return [left + 1, right + 1]

    return []



numbers = [-1,0]
target = -1
print(twoSum(numbers, target))