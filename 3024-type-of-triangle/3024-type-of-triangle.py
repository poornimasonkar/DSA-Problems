class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        a, b, c = nums

        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            return "none"

        if a == b == c:
            return "equilateral"

        elif a == b or b == c or a == c:
            return "isosceles"

        return "scalene"