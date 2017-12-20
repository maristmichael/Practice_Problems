"""
Self-Dividing Numbers from @LeetCode.com
----------------------------------------

A self-dividing number is a number that is divisible by every digit it contains.
e.g. 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number must not a zero digit.
Given a lower & upper number bound, output a list of every possible self dividing number from 1 to 1000
"""

class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        # Returning a list as the solution
        answer = []

        # Helper function that determines length of an int, returns an int
        def int_len(n):
            if abs(n) < 10:
                return 1
            return 1 + int_len(n/10)

        for number in range(left, right+1):
            # If the int is one digit and not 0, immediately append it to answer[]
            if int_len(number) == 1 and number != 0:
                answer.append(number)
            else:
                # Create a temporary list containing the digits of the number to modulus
                digits = list(map(int, str(number)))
                for k in range(len(digits)):
                    # If the digit is 0 or has a remainder when modulating a number, break to the next iteration
                    if digits[k] == 0:
                        break
                    if number % digits[k] != 0:
                        break
                    # Append the number if its the last digit and there is not remainder when modulating
                    if k == len(digits)-1 and number % digits[k] < 1:
                        answer.append(number)
                        break
                    continue
                # Clear the list after traversing the number
                digits.clear()
        return answer

# Test
test = Solution()
print(test.selfDividingNumbers(1, 1000))
