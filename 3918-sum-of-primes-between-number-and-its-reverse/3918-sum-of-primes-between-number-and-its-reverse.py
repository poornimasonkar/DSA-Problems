class Solution(object):
    def sumOfPrimesInRange(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Reverse the number
        rev = 0
        temp = n

        while temp > 0:
            rev = rev * 10 + temp % 10
            temp //= 10

        start = min(n, rev)
        end = max(n, rev)

        total = 0

        # Check every number in the range
        for num in range(start, end + 1):

            if num < 2:
                continue

            is_prime = True

            i = 2
            while i * i <= num:
                if num % i == 0:
                    is_prime = False
                    break
                i += 1

            if is_prime:
                total += num

        return total