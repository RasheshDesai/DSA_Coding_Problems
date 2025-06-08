# Method 1: Using a for loop to find max and min
def findSum(arr):

    if len(arr) == 0:
        return 0
    arr.max()
    max_val = arr[0]
    min_val = arr[0]
    print(max_val, min_val)
    num = 0
    for num in arr:
        if num > max_val:
            max_val = num
        elif num < min_val:
            min_val = num
    return max_val - min_val

print(findSum([1, -2, 3, 4, 5])) 


# Method 2: Using built-in functions

def findSum2(arr):
    if len(arr) == 0:
        return 0
    
    max_val = max(arr)
    min_val = min(arr)
    return max_val - min_val
print(findSum2([1, -2, 3, 4, 5]))


