# def kLengthApart(nums, k):
#     prev = -1  # stores index of the previous 1
#     for i in range(len(nums)):
#         if nums[i] == 1:
#             if prev != -1 and i - prev - 1 < k:
#                 return False
#             prev = i
#     return True


# nums = [1, 0, 1, 0, 0, 1]
# k = 2
# print(kLengthApart(nums, k))



def merger(nums1, m, nums2, n):
    new_list = nums1[:m] + nums2[:n]
    new_list.sort()
    return new_list

print(merger(nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3))