class Solution:
    def maxArea(self, height: List[int]) -> int:
        s = 0
        f = len(height) - 1

        max_area = 0

        while (s < f):
            area = min(height[f], height[s]) * (f-s)

            max_area = max(max_area, area)

            if height[f] > height[s]:
                s += 1
            else:
                f -= 1

        return max_area