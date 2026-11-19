class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval: interval[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if start <= res[-1][1]:
                res[-1][1] = max(end, res[-1][1])
            else:
                res.append(intervals[i])
        return res
