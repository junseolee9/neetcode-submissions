class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1
        res = 0
        while i < j:
            maxi = min(heights[i], heights[j]) * abs(i-j)
            if heights[i] < heights[j]:
                i += 1
                res = max(res, maxi)
            else:
                j -= 1
                res = max(res, maxi)

        return res
                    
