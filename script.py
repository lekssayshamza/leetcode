def first_day_reaching(production, target):
    left = 0
    right = len(production) - 1

    while left < right:
        mid = (left + right) // 2
        if target <= production[mid]:
            right = mid
        else:
            left = mid + 1

    if production and target <= production[right]:
        return right

    return -1



production = [5, 12, 19, 19, 27, 35, 42, 42, 50]

print(first_day_reaching(production, 19))  # 2
print(first_day_reaching(production, 20))  # 4
print(first_day_reaching(production, 42))  # 6
print(first_day_reaching(production, 60))  # -1
print(first_day_reaching([], 10))          # -1
print(first_day_reaching([5, 12, 19, 19, 19, 27, 35], 19))  # 2
print(first_day_reaching([15], 10))                            # 0
print(first_day_reaching([15], 20))                            # -1
print(first_day_reaching([15], 15))                            # 0
print(first_day_reaching([5, 5, 5, 5], 5))                      # 0