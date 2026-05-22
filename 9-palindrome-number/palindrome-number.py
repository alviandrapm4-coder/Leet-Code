class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #alviandrapiero
        return str(x) == str(x)[::-1]