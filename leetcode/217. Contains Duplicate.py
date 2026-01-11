from typing import List


class Solution:
    def containsDuplicate_brute(self, nums: List[int]) -> bool:
        for i, n in enumerate(nums):
            if n in nums[i + 1 :]:
                return True
        return False

    def containsDuplicate_sort(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
