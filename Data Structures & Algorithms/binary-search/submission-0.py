class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:        #until left and right points to same number
            mid = (left +right)//2
            if nums[mid] > target:
                right = mid - 1     #move right to first half
            elif nums[mid] < target:
                left = mid + 1      #move left to next half
            else:
                return mid

        return -1