class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = []
        while (left <= right):
            if (height[left] <= height[right]):
                max_area.append(((right - left) * height[left]))
                left += 1
            else:
                max_area.append(((right - left) * height[right]))
                right -= 1
        return max(max_area)
