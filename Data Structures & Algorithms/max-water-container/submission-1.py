class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 2 ptrs -> start from the ends
        # calculate curr area using heights & diff between ptrs
        # update max if applicable
        # move the ptr that's smaller
        # repeat

        l = 0
        r = len(heights) - 1
        maxArea = 0

        while l < r:
            maxArea = max(maxArea, (r - l) * min(heights[l], heights[r]))

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea