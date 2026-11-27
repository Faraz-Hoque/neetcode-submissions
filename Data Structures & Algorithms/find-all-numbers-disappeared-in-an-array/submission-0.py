class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #iterating through the list
        for i in range(len(nums)):
            #range starts from 1
            temp = abs(nums[i]) - 1
            #if element is positive
            if nums[temp] > 0:
                nums[temp] *= -1  

        res = []
        for i,n in enumerate(nums):
            if n > 0:
                res.append(i+1)

        return res