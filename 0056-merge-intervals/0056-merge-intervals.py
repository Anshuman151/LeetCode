class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for i in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not res or res[-1][1] < i[0]:
                res.append(i)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                res[-1][1] = max(res[-1][1], i[1])

        return res