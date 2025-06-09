def find_insert_position(nums, target):
    left = 0
    right =len(nums)-1
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

# Example
my_list = [10, 20, 30, 40]
target = 40
print(find_insert_position(my_list, target))  # Output: 1
