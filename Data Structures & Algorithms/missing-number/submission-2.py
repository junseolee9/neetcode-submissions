class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        key = 0
        for i in range(len(nums)):
            if key not in nums:
                return key
            else:
                key += 1
        return key