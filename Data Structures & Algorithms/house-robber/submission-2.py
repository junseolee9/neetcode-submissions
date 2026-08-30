class Solution:
    def rob(self, nums: List[int]) -> int:
        l, r = 0, 0
        for num in nums:
            temp = max(num + l, r)
            l = r
            r = temp
        return r