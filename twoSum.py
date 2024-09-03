from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):

                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]

        return []
            

sol = Solution()
print(sol.twoSum([1, 2, 3, 4], 6))