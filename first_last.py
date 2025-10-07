from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums, target):
            start, end = 0, len(nums) - 1
            idx = -1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    idx = mid
                    end = mid - 1   # keep searching left
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return idx

        def findLast(nums, target):
            start, end = 0, len(nums) - 1
            idx = -1
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    idx = mid
                    start = mid + 1   # keep searching right
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return idx

        first = findFirst(nums, target)
        last = findLast(nums, target)
        return [first, last]
