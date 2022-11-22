class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for m in range(len(nums)):
                if i < m:
                    if nums[i]+nums[m] == target:
                        return [i,m]
