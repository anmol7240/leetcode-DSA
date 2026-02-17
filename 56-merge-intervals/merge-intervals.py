class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()

        merge = []

        for i in range(n):
            start = intervals[i][0]
            end = intervals[i][1]

            if not merge or merge[-1][1] < start:
                merge.append([start,end])
            else:
                merge[-1][1] = max(merge[-1][1], end)

        return merge
