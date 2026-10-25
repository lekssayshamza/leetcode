# link: https://leetcode.com/problems/range-sum-query-immutable/

def build_prefix(nums):
    prefix = [0]

    for num in nums:
        prefix.append(prefix[-1] + num)

    return prefix

def range_sum(prefix, left, right):
    return prefix[right + 1] - prefix[left]


prefix = [0, 3, 4, 9, 11, 17]

print(range_sum(prefix, 1, 4))
print(range_sum(prefix, 2, 3))
print(range_sum(prefix, 0, 4))