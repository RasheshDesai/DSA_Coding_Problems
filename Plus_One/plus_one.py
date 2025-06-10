
# def plusOne(digits):
#     for i in [len(digits)-1]:
#         digits[i] = digits[i] + 1
#         if len(str(digits[i])) >= 10:
#             #break it into 2 and add them in the list (same list)
            
            
#     return digits

# print(plusOne(digits=[1,2,3,9]))

def findElement(nums,target):
    for i in iter(nums):
        if nums[i] == target:
            print(f"Your target is at location {i}")
            return
    print("Target not found")

findElement(nums=[1,2,3,10,15],target=2
)