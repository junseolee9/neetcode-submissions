class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    continue
                else:
                    return nums[j]
        return nums[0]
