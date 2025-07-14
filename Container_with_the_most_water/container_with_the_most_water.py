def maxArea(height):

    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        height_left = height[left]
        height_right = height[right]
        width = right - left
        area = min(height_left, height_right) * width
        max_area = max(max_area, area)

        if height_left < height_right:
            left += 1
        else:
            right -= 1


    return max_area


print(maxArea(height = [1,2,3,4,5]))
