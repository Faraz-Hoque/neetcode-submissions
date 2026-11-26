class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #iterate theough the array -> for n in nums
        # add each to total  -> sum(range(len(nums) + 1))
        #if not matched wiht expected total -> sum(nums)
        #mark at which number didnt match  
        #return that number
        return sum(range(len(nums) + 1)) - sum(nums)