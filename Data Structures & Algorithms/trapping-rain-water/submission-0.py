class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = 0
        lhs = []

        for i in range(len(height)):
            curr_height = height[i]
            prefix = max(prefix, curr_height)
            lhs.append(max(prefix, curr_height))
        # print(lhs)
        
        suffix = 0
        rhs = []
        for j in range(len(height)-1, -1, -1):
            curr_height = height[j]
            suffix = max(suffix, curr_height)
            rhs.append(max(suffix, curr_height))
        rhs = rhs[::-1]
        # print(rhs)

        total = 0
        for i in range(len(height)):
            bar_height = height[i]
            trapped = min(lhs[i], rhs[i]) - bar_height
            total += trapped
            # print(trapped)

        return total

            
