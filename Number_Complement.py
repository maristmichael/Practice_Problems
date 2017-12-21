"""
Number Compliment from @LeetCode.com
------------------------------------

Given a positive integer, output its unsigned complement number.
The complement strategy is to flip the bits of its binary representation.

** The given integer fits within a 32-bit signed integer range.
** No leading 0's

"""

class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        binary_num = bin(num)[2:]                              # Convert the int to binary & remove first 2 characters
        output = int('1' * len(binary_num)) - int(binary_num)  # Negate bin. number with (1-bits * size of bin. number)
        return int(str(output), 2)                             # Convert the str of bin. num into an int & return it

#  Test Cases:
#
#  Int --> newInt | Binary --> newBinary
#  ----------------------------
#  17 --> 14 | 10001 --> 01110
#  4  -->  3 |   100 -->   011

test = Solution()
print(test.findComplement(17))
print(test.findComplement(4))
