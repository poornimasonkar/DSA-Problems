class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        binary = bin(n)[2:]
        for i in range(len(binary)):
            if binary[i] == '1':
                count += 1

        return count
        