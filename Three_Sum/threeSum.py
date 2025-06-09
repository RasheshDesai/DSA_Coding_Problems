class Solution(object):
    def threeSum(self,nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        finalList=[]
        nums.sort()

        for i, a in enumerate(nums):
                if i>0 and a == nums[i-1]:
                        continue
                
                l,r = i+1, len(nums)-1     ## i+1 => next element to i and len(nums) -1 -> last element of the list or array

                while l < r:
                        threeSum = a + nums[l] + nums[r]

                        if threeSum > 0:
                                r -= 1
                        elif threeSum < 0:
                                l += 1
                        else:
                                finalList.append([a,nums[l],nums[r]])
                                while l < r and nums[l] == nums[l + 1]:
                                    l += 1
                                while l < r and nums[r] == nums[r - 1]:
                                    r -= 1

                                # Move both pointers inward after handling the current triplet
                                l += 1
                                r -= 1

        return finalList
            