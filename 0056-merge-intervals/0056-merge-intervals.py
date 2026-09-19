class Solution(object):
    def merge(self, intervals):
        intervals.sort()

        merged = []

        A = intervals[0]

        for i in range(len(intervals) - 1):
            B = intervals[i + 1]

            if A[1] >= B[0]:
                A = [A[0], max(A[1], B[1])]
            else:
                merged.append(A)
                A = B

        merged.append(A)

        return merged