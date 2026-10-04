class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Special overflow case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        # Determine the sign
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:

            temp = divisor
            multiple = 1

            # Double divisor until it becomes too large
            while dividend >= temp + temp:
                temp += temp
                multiple += multiple

            # Subtract the largest possible chunk
            dividend -= temp
            quotient += multiple

        return -quotient if negative else quotient
        