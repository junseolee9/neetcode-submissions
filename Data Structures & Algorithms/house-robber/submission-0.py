class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(start):
            if start in memo:
                return memo[start]
            if not start < len(nums):
                memo[start] = 0
            else:
                memo[start] = max(nums[start] + dfs(start + 2), dfs(start + 1))
            return memo[start]
        return dfs(0)