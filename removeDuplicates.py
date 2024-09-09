from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] > nums[j]:
        #             nums[i], nums[j] = nums[j], nums[i]

        nums.sort()

        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        
        return k

sol = Solution()

nums = [1, 2, 1]
k = sol.removeDuplicates(nums)
print("Modified array:", nums[:k])    