"""
Self-Dividing Numbers from @LeetCode.com
----------------------------------------

A self-dividing number is a number that is divisible by every digit it contains.
e.g. 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number must not contain a zero digit.
Given a lower & upper number bound, output a list of every possible self dividing number from 1 to 1000
"""

class Solution:
    def self_dividing_numbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        answer = []  # Return this list as the solution

        for number in range(left, right+1):
            if int_len(number) == 1 and number != 0:  # If number is one digit AND not 0, append it to answer[]
                answer.append(number)
            else:
                digits = list(map(int, str(number)))  # Temporary list containing the digits of the number to modulus
                for k in range(len(digits)):
                    if digits[k] == 0 or number % digits[k] != 0:  # Break if digit is 0 OR there is a remainder
                        break
                    if k == len(digits)-1 and number % digits[k] < 1:  # Append number if on last digit & no remainder
                        answer.append(number)
                        break
                    continue
                digits.clear()  # Clear the list after traversing the number
        return answer

# Helper function that determines length of an int, returns an int
def int_len(n):
    if abs(n) < 10:
        return 1
    return 1 + int_len(n/10)

# Test
test = Solution()
print(test.self_dividing_numbers(1, 1000))
