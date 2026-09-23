class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        A = newInterval
        insert =[]
        for i in range(len(intervals)):
            B = intervals[i]

            if A[1] < B[0] :
                insert.append(A)
                A = B
            elif B[1] < A[0]:
                insert.append(B)

            else:
                A = [min(A[0],B[0]),max(A[1],B[1])]
            

        insert.append(A)
        return insert

                