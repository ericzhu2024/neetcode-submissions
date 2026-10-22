class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 首尾加哨兵
        heights = [0] + heights + [0]
        stack = []  # 单调递增栈，存下标
        max_area = 0

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                top = stack.pop()
                # 左边界是当前栈顶，右边界是 i
                width = i - stack[-1] - 1
                max_area = max(max_area, heights[top] * width)
            stack.append(i)

        return max_area