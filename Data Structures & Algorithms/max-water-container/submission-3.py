class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # max_height = max(heights)
        # max_width = len(heights)
        # max_area = 0

        # for i in range(len(heights)):
        #     x0 = i
        #     y0 = heights[i]

        #     for j in range(len(heights) -1, i, -1):
        #         if max_area // j > heights[j]:
        #             continue

        #         x1 = j
        #         y1 = heights[j]

        #         height = min(y0, y1)
        #         width = x1 - x0
        #         area = height * width
        #         if area > max_area: 
        #             max_area = area
        
        # return max_area
        l, r = 0, len(heights)-1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            res = max(res, area)
            
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return res
            




        