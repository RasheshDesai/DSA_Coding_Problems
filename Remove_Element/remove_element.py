class Solution(object):
    def removeElement(self, nums, val):
        k = 0  # Index to place the next valid element
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        # Replace the remaining elements with underscores for display
        for i in range(k, len(nums)):
            nums[i] = '_'

        return k