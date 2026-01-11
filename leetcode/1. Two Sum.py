from typing import List


class Solution:
    def twoSum_brute(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return [-1, -1]

    def twoSum_sort(self, nums: List[int], target: int) -> List[int]:
        nums = [(v, i) for i, v in enumerate(nums)]  # ty:ignore[invalid-assignment]
        nums.sort()
        l, r = 0, len(nums) - 1  # noqa: E741
        while l < r:
            summ = nums[l][0] + nums[r][0]  # ty:ignore[not-subscriptable]
            if summ == target:
                return sorted([nums[l][1], nums[r][1]])  # ty:ignore[not-subscriptable]

            elif summ < target:
                l += 1  # noqa: E741
            else:
                r -= 1

        return [-1, -1]

    def twoSum_optimal(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i, n in enumerate(nums):
            comp = target - n
            if comp in mp:
                return [mp[comp], i]

            mp[n] = i

        return [-1, -1]
