def singleNumber(nums):

    for i in range(len(nums)):
        current = []
        for j in range(i,len(nums)):
            if nums[j] != nums[i]:
                current.append(nums[j])

                
            if len(current) > 1:
                current = []
    return print(current)

singleNumber(nums=[1,1,2,2,4])

