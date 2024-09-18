from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if target <= nums[0]:
                return 0
        
        for i in range(len(nums) - 1):
            if target == nums[i]:
                return i
            
            elif target > nums[i] and target <= nums[i + 1]:
                return i + 1
        
        return len(nums)
    
sol = Solution()


arr = [1,3,5,6]
tar = 3
print(sol.searchInsert(arr, tar))