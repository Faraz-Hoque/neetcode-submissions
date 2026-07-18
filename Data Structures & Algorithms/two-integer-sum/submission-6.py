class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Solution with HashMap since the array is unsorted

        seen ={}   # stores {number: index}
        #Setting i=index and num=value from the given array
        #using enumerate()
        for i, num in enumerate(nums):   
            complement = target - num  # since num+complement = target
            if complement in seen:     # check in the empty dict
                return [seen[complement],i]  #return the index of the complement and the index of the num
            seen[num] = i       #store the index after check